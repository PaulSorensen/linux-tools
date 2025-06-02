from typing import List, Tuple, Dict, Optional
from helper.data_helper import DataHelper
from helper.prompt_helper import PromptHelper

class OrderHelper:
    """Helper for managing ordering of sections and categories."""
    
    @staticmethod
    def validate_order_input(order_string: str, max_items: int) -> Tuple[bool, str, List[int]]:
        """Validates order input string."""
        try:
            numbers = [int(x.strip()) for x in order_string.replace(" ", "").split(",")]
        except ValueError:
            return False, DataHelper.sanitize(PromptHelper.invalid_input()) + ": Please use numbers separated by commas", []

        if not numbers:
            return False, "No numbers provided", []
            
        if len(numbers) != len(set(numbers)):
            return False, DataHelper.sanitize(PromptHelper.invalid_input()) + ": Duplicate numbers found", []
            
        if any(n < 1 or n > max_items for n in numbers):
            return False, DataHelper.sanitize(PromptHelper.invalid_input()) + f": Numbers must be between 1 and {max_items}", []
            
        return True, "", numbers

    @staticmethod
    def clean_title(section_data: Dict) -> str:
        """Get clean title from section or category data."""
        if isinstance(section_data, dict):
            if 'name' in section_data:  # Category
                return section_data['name']
            else:  # Section
                return list(section_data.keys())[0]
        return section_data
    
    @staticmethod
    def get_sort_key(item_name, order_value):
        """Get sort key for an item based on order value."""
        if order_value is not None:
            return (0, order_value)  # Use the order number
        return (1, item_name)  # Alphabetical after ordered items       

    @staticmethod
    def get_order(item: Dict) -> Optional[int]:
        """Get order from section or category data."""
        if isinstance(item, dict):
            if 'name' in item:  # Category
                return item.get('order')  # Will return None if not set
            else:  # Section
                section_name = list(item.keys())[0]
                return item[section_name].get('order')  # Will return None if not set
        return None

    @staticmethod
    def set_order(item: Dict, order: Optional[int]) -> Dict:
        """Set order for section or category."""
        if isinstance(item, dict):
            if 'name' in item:  # Category
                item['order'] = order
            else:  # Section
                section_name = list(item.keys())[0]
                item[section_name]['order'] = order
        return item
    
    @staticmethod
    def sort_items(items: List) -> List:
        """Sort items by order number, then alphabetically."""
        def sort_key(item):
            order = OrderHelper.get_order(item)
            title = OrderHelper.clean_title(item)
            return (not bool(order), title)  # Ordered items first, then alphabetical
            
        return sorted(items, key=sort_key)