import yaml
from ruamel.yaml import YAML
from typing import List, Dict
from pathlib import Path
from helper.order_helper import OrderHelper

class Category:
    """Model for category data operations."""
    
    def __init__(self):
        self.data_file = Path("data/structure.yaml")
    
    def get_all(self) -> Dict:
        """Get all categories grouped by section."""
        try:
            with open(self.data_file, 'r') as f:
                return yaml.safe_load(f) or {}
        except FileNotFoundError:
            return {}
    
    def get_by_section(self, section: str) -> List[Dict]:
        """Get categories for a specific section."""
        structure = self.get_all()
        return structure.get(section, {}).get('categories', [])
    
    def add(self, section: str, category_name: str) -> bool:
        """Add a new category to a section"""
        structure = self.get_all()
        if section not in structure:
            structure[section] = {'order': None, 'categories': []}
        
        categories = structure[section]['categories']
        if not any(cat['name'] == category_name for cat in categories):
            categories.append({
                'name': category_name,
                'order': None
            })
            self._save(structure)
            return True
        return False
    
    def delete(self, section: str, category_name: str) -> bool:
        """Delete a category and its tools"""
        structure = self.get_all()
        if section in structure:
            categories = structure[section]['categories']
            for i, cat in enumerate(categories):
                if cat['name'] == category_name:
                    categories.pop(i)
                    self._save(structure)
                    
                    # Delete all tools in category
                    from model.tool import Tool
                    Tool().delete_by_section_category(section, category_name)
                    return True
        return False
    
    def save_order(self, section: str, ordered_categories: List[str]) -> bool:
        """Save new category order."""
        try:
            with open(self.data_file, 'r') as f:
                structure = yaml.safe_load(f) or {}
            
            if section in structure:
                categories = structure[section]['categories']
                for i, cat_name in enumerate(ordered_categories, 1):
                    for cat in categories:
                        if cat['name'] == cat_name:
                            cat['order'] = i
                            break
                
                self._save(structure)
                return True
            return False
        except Exception as e:
            print(f"Error saving category order: {e}")
            return False
    
    def _save(self, structure: Dict) -> None:
        """Save structure to file with clean formatting."""

        # Ensure clean formatting with ruamel.yaml
        yaml = YAML()
        yaml.indent(mapping=2, sequence=4, offset=2)
        yaml.default_flow_style = False
        yaml.allow_unicode = True
        yaml.width = 4096  # Prevent line wrapping

        with open(self.data_file, 'w', encoding='utf-8') as f:
            yaml.dump(structure, f)