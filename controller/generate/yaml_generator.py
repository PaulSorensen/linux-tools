from ruamel.yaml import YAML
from model.tool import Tool
from helper.order_helper import OrderHelper
from helper.layout_helper import LayoutHelper

class YamlGenerator:
    """Generates YAML output of all tools."""

    filename = "linux-tools.yaml"
    
    def __init__(self):
        self.tool_model = Tool()
    
    def generate(self):
        """Generate YAML file."""
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
        output = {}
        for section in sorted_sections:
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
            
            output[section] = {}
            for category in sorted_categories:
                tools_sorted = sorted(grouped[section][category], key=lambda t: t['title'])
                output[section][category] = [
                    {
                        'title': t['title'],
                        'description': t['description'],
                        'url': t['url'],
                        # Sort tags alphabetically
                        'tags': sorted(t['tags']) if isinstance(t['tags'], list) else t['tags']
                    }
                    for t in tools_sorted
                ]
        
        # Wrap output with top-level key
        output = {LayoutHelper.app_name().upper(): output}

        # Ensure clean formatting with ruamel.yaml
        yaml = YAML()
        yaml.indent(mapping=2, sequence=4, offset=2)
        yaml.default_flow_style = False
        yaml.allow_unicode = True
        yaml.width = 4096  # Prevent line wrapping

        # Write output to file
        with open(self.filename, 'w', encoding='utf-8') as f:
            yaml.dump(output, f)