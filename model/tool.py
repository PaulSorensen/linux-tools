import yaml
from ruamel.yaml import YAML
from typing import List, Dict
from pathlib import Path

class Tool:
    """Model for tool data operations."""
    
    # Define tool field order as a class attribute
    tool_fields = [
        'title',
        'section', 
        'category',
        'description',
        'url',
        'tags'
    ]
    
    def __init__(self):
        self.data_file = Path("data/tools.yaml")
        self.structure_file = Path("data/structure.yaml")
    
    def get_all(self) -> List[Dict]:
        """Get all tools."""
        try:
            with open(self.data_file, 'r') as f:
                return yaml.safe_load(f) or []
        except FileNotFoundError:
            return []
    
    def get_structure(self) -> Dict:
        """Get structure configuration."""
        try:
            with open(self.structure_file, 'r') as f:
                return yaml.safe_load(f) or {}
        except FileNotFoundError:
            return {}        
    
    def get_by_section_category(self, section: str, category: str) -> List[Dict]:
        """Get tools for a specific section and category."""
        tools = self.get_all()
        return [tool for tool in tools 
                if tool.get('section') == section 
                and tool.get('category') == category]
    
    def _create_ordered_tool(self, tool_data: Dict) -> Dict:
        """Create a tool with consistent field ordering."""
        return {
            field: tool_data.get(field, [] if field == 'tags' else None)
            for field in self.tool_fields
        }
    
    def add(self, tool_data: Dict) -> None:
        """Add a new tool."""
        tools = self.get_all()
        tools.append(self._create_ordered_tool(tool_data))
        self._save(tools)
    
    def delete(self, tool_to_delete: Dict) -> None:
        """Delete a specific tool."""
        tools = self.get_all()
        # Find and remove the exact tool
        for i, tool in enumerate(tools):
            if (tool.get('title') == tool_to_delete.get('title') and 
                tool.get('section') == tool_to_delete.get('section') and
                tool.get('category') == tool_to_delete.get('category')):
                tools.pop(i)
                break
        self._save(tools)
    
    def delete_by_section(self, section: str) -> None:
        """Delete all tools in a section."""
        tools = self.get_all()
        tools = [tool for tool in tools if tool.get('section') != section]
        self._save(tools)
    
    def delete_by_section_category(self, section: str, category: str) -> None:
        """Delete all tools in a section/category."""
        tools = self.get_all()
        tools = [tool for tool in tools 
                if not (tool.get('section') == section 
                       and tool.get('category') == category)]
        self._save(tools)
    
    def validate_section_category(self, section: str, category: str) -> bool:
        """Validate section and category exist in structure."""
        try:
            with open(self.structure_file, 'r') as f:
                structure = yaml.safe_load(f) or {}
            
            if section not in structure:
                return False
                
            categories = structure[section]['categories']
            return any(cat['name'] == category for cat in categories)
        except FileNotFoundError:
            return False
    
    def _save(self, tools: List[Dict]) -> None:
        """Save tools to file."""
        output = [self._create_ordered_tool(tool) for tool in tools]

        # Ensure clean formatting with ruamel.yaml
        yaml = YAML()
        yaml.indent(mapping=2, sequence=4, offset=2)
        yaml.default_flow_style = False
        yaml.allow_unicode = True
        yaml.width = 4096  # Prevent line wrapping

        # Write output to file
        with open(self.data_file, 'w', encoding='utf-8') as f:
            yaml.dump(output, f)