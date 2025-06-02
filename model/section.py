import yaml
from ruamel.yaml import YAML
from pathlib import Path

class Section:
    """Model for section data operations."""
    
    def __init__(self):
        self.data_file = Path("data/structure.yaml")
    
    def get_all(self):
        """Get all sections."""
        try:
            with open(self.data_file, 'r') as f:
                structure = yaml.safe_load(f) or {}
                return list(structure.keys())
        except FileNotFoundError:
            return []
    
    def add(self, section_name):
        """Add a new section."""
        try:
            with open(self.data_file, 'r') as f:
                structure = yaml.safe_load(f) or {}
                
            if section_name not in structure:
                structure[section_name] = {
                    'order': None,
                    'categories': []                    
                }
                self._save(structure)
                return True
            return False
        except FileNotFoundError:
            structure = {
                section_name: {
                    'order': None,
                    'categories': []                    
                }
            }
            self._save(structure)
            return True
    
    def delete(self, section_name):
        """Delete a section and all its categories and their tools."""
        try:
            with open(self.data_file, 'r') as f:
                structure = yaml.safe_load(f) or {}
            
            if section_name in structure:
                # Store categories before deletion
                categories = [cat['name'] for cat in structure[section_name].get('categories', [])]
                
                # Delete section from structure
                del structure[section_name]
                self._save(structure)
                
                # Delete all tools in each category
                from model.tool import Tool
                tool_model = Tool()
                for category in categories:
                    tool_model.delete_by_section_category(section_name, category)
                
                return True
            return False
        except FileNotFoundError:
            return False
    
    def save_order(self, sections: list) -> bool:
        """Save new section order."""
        try:
            with open(self.data_file, 'r') as f:
                structure = yaml.safe_load(f) or {}
            
            # Update order values in structure
            for i, section in enumerate(sections, start=1):
                if section in structure:
                    structure[section]['order'] = i
            
            self._save(structure)
            return True
        except FileNotFoundError:
            return False
    
    def _save(self, structure):
        """Save structure to file"""

        # Ensure clean formatting with ruamel.yaml
        yaml = YAML()
        yaml.indent(mapping=2, sequence=4, offset=2)
        yaml.default_flow_style = False
        yaml.allow_unicode = True
        yaml.width = 4096  # Prevent line wrapping

        with open(self.data_file, 'w', encoding='utf-8') as f:
            yaml.dump(structure, f)