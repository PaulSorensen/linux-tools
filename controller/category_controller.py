from pathlib import Path
from model.section import Section
from model.category import Category
from helper.layout_helper import LayoutHelper
from helper.prompt_helper import PromptHelper
from helper.data_helper import DataHelper

class CategoryController:
    """Controller for category operations."""
    
    def __init__(self):
        self.section_model = Section()
        self.category_model = Category()
    
    def add(self):
        """Add a new category."""
        # Select section
        section = self._select_section("Choose a section:")
        if not section:
            return

        while True:
            LayoutHelper.clear()
            LayoutHelper.header()
            print(f"Section: {section}")

            # Get existing categories and format them for display
            categories = self.category_model.get_by_section(section)
            category_names = [cat['name'] for cat in categories]
            categories_str = ", ".join(sorted(category_names))

            if categories_str:
                print(f"Existing categories: {categories_str}")

            # Get new category name
            print()
            category = DataHelper.title_case(input("Category name: ").strip())

            if not category:
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
                continue  # Show fresh page
            else:
                self.category_model.add(section, category)
                print()
                print(f"Added category '{category}' to section '{section}'")
                print()
                input(PromptHelper.enter_main_menu())
                break
    
    def delete(self):
        """Delete a category."""
        # Select section
        section = self._select_section("Select from which section to delete a category:")
        if not section:
            return

        while True:
            LayoutHelper.clear()
            LayoutHelper.header()
            print(f"Section: {section}")

            categories = self.category_model.get_by_section(section)
            if not categories:
                print()
                print("No categories available in this section.")
                print()
                input(PromptHelper.enter_main_menu())
                return

            print()
            print("Warning: This will delete selected category and all its tools!")
            print("Select what category to delete:")
            print()

            # Sort categories by name
            sorted_categories = sorted(categories, key=lambda x: x['name'])
            for i, category in enumerate(sorted_categories, 1):
                print(f"{i}) {category['name']}")
            print()

            choice = input(PromptHelper.choose_option()).strip()

            try:
                category_to_delete = sorted_categories[int(choice.strip()) - 1]['name']
                self.category_model.delete(section, category_to_delete)
                print()
                print(f"Deleted: '{category_to_delete}' and all its tools")
                print()
                input(PromptHelper.enter_main_menu())
                break  # Exit after successful delete
            except (ValueError, IndexError):
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
                continue  # Show fresh page

    # ─────────────────────────────────────────────
    # Private helper methods
    # ─────────────────────────────────────────────             
    
    def _select_section(self, prompt):
        """Helper method to select a section."""
        while True:
            LayoutHelper.clear()
            LayoutHelper.header()
            
            sections = self.section_model.get_all()
            if not sections:
                print("No sections and categories available.")
                print()
                input(PromptHelper.enter_main_menu())
                return None
                
            print(prompt)
            print()
            sorted_sections = sorted(sections)
            for i, section in enumerate(sorted_sections, 1):
                print(f"{i}) {section}")
            print()
            
            choice = input(PromptHelper.choose_option()).strip()
            try:
                return sorted_sections[int(choice.strip()) - 1]
            except (ValueError, IndexError):
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
                # Loop continues for another try