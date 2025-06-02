import os
from model.tool import Tool
from helper.order_helper import OrderHelper
from helper.layout_helper import LayoutHelper

class MarkdownGenerator:
    """Generates Markdown output of all tools."""

    filename = "linux-tools.md"
    
    def __init__(self):
        self.tool_model = Tool()
    
    def generate(self):
        """Generate markdown file."""
        tools = self.tool_model.get_all()
        structure = self.tool_model.get_structure()
        
        # Group tools by section and category
        grouped = {}
        for tool in tools:
            section = tool['section']
            category = tool['category']
            grouped.setdefault(section, {}).setdefault(category, []).append(tool)
        
        # Sort sections by their order value (If order value = None, sort last)
        sorted_sections = sorted(grouped.keys(), 
                               key=lambda s: OrderHelper.get_sort_key(s, structure.get(s, {}).get('order', None)))

        # Build output structure
        output = f"# {LayoutHelper.app_name().upper()}\n\n"     
        for section in sorted_sections:
            output += f"## {section}\n\n"
            
            # Get categories and their order value for each section
            section_config = structure.get(section, {})
            categories_config = section_config.get('categories', [])
            
            # Map each category name to its order value
            category_orders = {}
            for cat_config in categories_config:
                cat_name = cat_config.get('name')
                cat_order = cat_config.get('order', None)
                if cat_name:
                    category_orders[cat_name] = cat_order
            
            # Sort categories by their order value (If order value = None, sort last)
            sorted_categories = sorted(grouped[section].keys(), 
                                     key=lambda c: OrderHelper.get_sort_key(c, category_orders.get(c, None)))
            
            for category in sorted_categories:
                output += f"### {category}\n\n"
                tools_sorted = sorted(grouped[section][category], key=lambda t: t['title'])
                
                for tool in tools_sorted:
                    tags = tool.get('tags', [])
                    # Sort tags alphabetically
                    tags_str = ", ".join(f"`{tag}`" for tag in sorted(tags)) if tags else ""
                    output += f"* [**{tool['title']}**]({tool['url']}) - {tool['description']}"
                    if tags_str:
                        output += f"  \n  **Tags:** {tags_str}"
                    output += "\n"
                output += "\n"
        
        # Write output to file
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(output.rstrip() + '\n')