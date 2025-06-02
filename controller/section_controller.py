from pathlib import Path
from model.section import Section
from helper.layout_helper import LayoutHelper
from helper.prompt_helper import PromptHelper
from helper.data_helper import DataHelper

class SectionController:
    """Controller for section operations."""
    
    def __init__(self):
        self.section_model = Section()
    
    def add(self):
        """Add a new section."""
        while True:
            LayoutHelper.clear()
            LayoutHelper.header()

            # Show current sections
            sections = self.section_model.get_all()
            if sections:
                sections_str = ", ".join(sorted(sections))
                print(f"Sections: {sections_str}")
            else:
                print("Sections: (none)")
            print()

            section = DataHelper.title_case(input("Enter a new section to add: ").strip())

            if not section:
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
                continue  # Show fresh page

            if self.section_model.add(section):
                print()
                print(f"Added: '{section}' to sections")
                print()
                input(PromptHelper.enter_main_menu())
                break  # Exit after successful add
            else:
                print()
                print(f"Section '{section}' already exists!")
                print()
                input(PromptHelper.enter_try_again())
                # Loop continues, so fresh page is shown
    
    def delete(self):
        """Delete a section."""
        while True:
            LayoutHelper.clear()
            LayoutHelper.header()
            
            sections = self.section_model.get_all()
            if not sections:
                print("No sections available.")
                print()
                input(PromptHelper.enter_main_menu())
                return

            print("Warning: This will delete selected section and all its categories and their tools!")
            print("Select what section to delete:")
            print()
            sorted_sections = sorted(sections)
            for i, section in enumerate(sorted_sections, 1):
                print(f"{i}) {section}")
            print()

            choice = input(PromptHelper.choose_option()).strip()
            
            try:
                section_to_delete = sorted_sections[int(choice) - 1]
            except (ValueError, IndexError):
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
                continue  # Show fresh page

            self.section_model.delete(section_to_delete)
            print()
            print(f"Deleted: '{section_to_delete}' and all its categories and their tools")
            print()
            input(PromptHelper.enter_main_menu())
            break  # Exit after successful delete