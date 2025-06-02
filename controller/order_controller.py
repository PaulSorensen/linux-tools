from helper.layout_helper import LayoutHelper
from helper.prompt_helper import PromptHelper
from helper.order_helper import OrderHelper
from model.section import Section
from model.category import Category

class OrderController:
    """Controller for order operations."""
    def __init__(self):
        self.section_model = Section()
        self.category_model = Category()

    def run(self):
        """Display mange order menu and handle selection."""
        while True:
            LayoutHelper.clear()
            LayoutHelper.header()
            
            print("1) Reorder Sections")
            print("2) Reorder Categories") 
            print("0) Back to Main Menu")
            print()
            
            choice = input(PromptHelper.choose_option()).strip()
            
            if choice == "1":
                self.reorder_sections()
                break
            elif choice == "2":
                self.reorder_categories()
                break
            elif choice == "0":
                break
            else:
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
    
    def reorder_sections(self):
        """Reorder sections."""
        LayoutHelper.clear()
        LayoutHelper.header()
        
        sections = self.section_model.get_all()
        if not sections:
            print()
            print("No sections to reorder.")
            print()
            input(PromptHelper.return_main_menu())
            return
        
        # Display current order
        print("Current order:")
        sorted_sections = OrderHelper.sort_items(sections)
        for i, section in enumerate(sorted_sections, start=1):
            clean_title = OrderHelper.clean_title(section)
            print(f"{i}) {clean_title}")
        print()
        
        # Get new order
        while True:
            order_sections = input("Enter new order (e.g. 1,2,3): ").strip()
            valid, error, numbers = OrderHelper.validate_order_input(order_sections, len(sections))
            
            if not valid:
                LayoutHelper.clear()
                LayoutHelper.header()
                # Redisplay current order
                print("Current order:")
                for i, section in enumerate(sorted_sections, start=1):
                    clean_title = OrderHelper.clean_title(section)
                    print(f"{i}) {clean_title}")
                print()
                print(f"{error}")
                print()
                continue
            
            # Apply new order
            reordered = []
            for i, num in enumerate(numbers):
                if 0 <= num-1 < len(sorted_sections):
                    reordered.append(sorted_sections[num-1])
            
            if len(reordered) == len(sections):
                if self.section_model.save_order(reordered):
                    print()
                    print("Sections reordered successfully!")
                else:
                    print()
                    print("Error saving new order!")
            else:
                print()
                print("Error: Invalid section numbers!")
            break
        
        print()
        input(PromptHelper.enter_main_menu())

    def reorder_categories(self):
        """Handle category reordering for a section."""
        LayoutHelper.clear()
        LayoutHelper.header()
        
        # Get sections
        sections = self.section_model.get_all()
        if not sections:
            print()
            print("No sections available.")
            print()
            input(PromptHelper.enter_main_menu())
            return
        
        # Display sections
        print("Choose a section:")
        print()
        sorted_sections = OrderHelper.sort_items(sections)
        for i, section in enumerate(sorted_sections, 1):
            clean_title = OrderHelper.clean_title(section)
            print(f"{i}) {clean_title}")
        print()
        
        # Get section choice
        choice = input(PromptHelper.choose_option()).strip()
        try:
            section = sorted_sections[int(choice.strip()) - 1]
            section_name = OrderHelper.clean_title(section)
        except (ValueError, IndexError):
            print()
            print("Invalid selection!")
            print()
            input(PromptHelper.enter_main_menu())
            return
        
        # Get and display categories
        categories = self.category_model.get_by_section(section_name)
        if not categories:
            print()
            print("No categories to reorder in this section.")
            print()
            input(PromptHelper.enter_main_menu())
            return
        
        LayoutHelper.clear()
        LayoutHelper.header()
        # Display current order
        print(f"Categories in '{section_name}':")
        print()
        sorted_categories = OrderHelper.sort_items(categories)
        for i, category in enumerate(sorted_categories, 1):
            clean_title = OrderHelper.clean_title(category)
            print(f"{i}) {clean_title}")
        print()
        
        # Get new order
        while True:
            order_categories = input("Enter new order (e.g. 1,2,3): ").strip()
            valid, error, numbers = OrderHelper.validate_order_input(order_categories, len(categories))
            
            if not valid:
                LayoutHelper.clear()
                LayoutHelper.header()
                # Redisplay current order
                print(f"Categories in '{section_name}':")
                print()
                for i, category in enumerate(sorted_categories, 1):
                    clean_title = OrderHelper.clean_title(category)
                    print(f"{i}) {clean_title}")
                print()
                print(f"{error}")
                print()
                continue
            
            # Apply new order
            reordered = []
            for i, num in enumerate(numbers):
                title = OrderHelper.clean_title(sorted_categories[num - 1])
                reordered.append(title)
            
            # Save new order
            self.category_model.save_order(section_name, reordered)
            print()
            print("Categories reordered successfully!")
            break
        
        print()
        input(PromptHelper.enter_main_menu())