from model.section import Section
from model.category import Category
from model.tool import Tool
from helper.layout_helper import LayoutHelper
from helper.prompt_helper import PromptHelper
from helper.data_helper import DataHelper

class ToolController:
    """Controller for tool operations."""
    
    def __init__(self):
        self.section_model = Section()
        self.category_model = Category()
        self.tool_model = Tool()
    
    def add(self):
        """Add a new tool."""
        # Select section
        section = self._select_section("Choose a section:")
        if not section:
            return

        while True:
            LayoutHelper.clear()
            LayoutHelper.header()
            print(f"Section: {section}")

            # Get and display categories
            categories = self.category_model.get_by_section(section)
            if not categories:
                print()
                print("No categories available in this section. Please add a category first.")
                print()
                input(PromptHelper.enter_main_menu())
                return

            print()
            print("Select a category to add a tool to:")
            print()

            # Sort and display categories by name
            sorted_categories = sorted(categories, key=lambda x: x['name'])
            for i, category in enumerate(sorted_categories, 1):
                print(f"{i}) {category['name']}")
            print()

            # Get category choice
            choice = input(PromptHelper.choose_option()).strip()
            try:
                category = sorted_categories[int(choice.strip()) - 1]['name']
                break  # Valid selection, exit loop
            except (ValueError, IndexError):
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
                continue  # Show fresh page

        # Clear screen and show header again after category selection
        LayoutHelper.clear()
        LayoutHelper.header()
        print(f"Section: {section}")
        print(f"Category: {category}")
        print()

        # Enter tool details
        while True:
            print("Enter tool details:")
            print()

            title = DataHelper.capitalize_all(input("Title: ").strip())
            if not title:
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
                # Show fresh page for tool details
                LayoutHelper.clear()
                LayoutHelper.header()
                print(f"Section: {section}")
                print(f"Category: {category}")
                print()
                continue

            description = DataHelper.capitalize_first(input("Description: ").strip())

            url = input("URL: ").strip().lower()
            if url:
                if url.startswith("http://"):
                    url = "https://" + url[len("http://"):]
                elif not url.startswith("https://"):
                    url = "https://" + url

                url = url.rstrip("/")

            tags_input = input("Tags: (comma-separated): ").strip().lower()
            tags = sorted([tag.strip() for tag in tags_input.split(',') if tag.strip()])
            
            # Create tool
            tool_data = {
                'title': title,            
                'description': description,
                'url': url,
                'tags': tags,
                'section': section,
                'category': category
            }
            
            self.tool_model.add(tool_data)
            print()
            print(f"Added: {title}")
            print()
            print(PromptHelper.enter_main_menu(), end="")
            input()
            break  # Exit after successful add
    
    def delete(self):
        """Delete a tool."""
        LayoutHelper.clear()
        LayoutHelper.header()        
        # Select section
        section = self._select_section("Select from which section to delete a tool:")
        if not section:
            return

        LayoutHelper.clear()
        LayoutHelper.header()    
        # Select category
        category = self._select_category(section, "Select from which category to delete a tool:")
        if not category:
            return

        LayoutHelper.clear()
        LayoutHelper.header()    
        # Show tools and delete
        tools = self.tool_model.get_by_section_category(section, category)
        if not tools:
            print("No tools available in this category.")
            print()
            input(PromptHelper.enter_main_menu())
            return

        while True:
            LayoutHelper.clear()
            LayoutHelper.header()
            print(f"Section: {section}")
            print(f"Category: {category}")
            print()
            print("Warning: This will delete selected tool!")
            print("Select what tool to delete:")
            print()
            for i, tool in enumerate(tools, 1):
                print(f"{i}) {tool['title']}")
            print()

            choice = input(PromptHelper.choose_option()).strip()

            try:
                tool_to_delete = tools[int(choice.strip()) - 1]
                self.tool_model.delete(tool_to_delete)
                print()
                print(f"Deleted: '{tool_to_delete['title']}'")
                print()
                input(PromptHelper.enter_main_menu())
                break  # Exit after successful delete
            except (ValueError, IndexError):
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
                # Loop continues, so fresh page is shown

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
                print("No sections, categories, and tools available.")
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
                index = int(choice) - 1
                if 0 <= index < len(sorted_sections):
                    return sorted_sections[index]
                else:
                    print()
                    print(PromptHelper.invalid_input())
                    print()
                    input(PromptHelper.enter_try_again())
                    continue
            except ValueError:
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
                continue
   
    def _select_category(self, section, prompt):
        """Helper method to select a category."""
        while True:
            LayoutHelper.clear()
            LayoutHelper.header()
            print(f"Section: {section}")
                
            categories = self.category_model.get_by_section(section)
            if not categories:
                print()
                print("No categories and tools available in this section.")
                print()
                input(PromptHelper.enter_main_menu())
                return None

            print()    
            print(prompt)
            print()
            # Sort categories by name
            sorted_categories = sorted(categories, key=lambda x: x['name'])
            for i, category in enumerate(sorted_categories, 1):
                print(f"{i}) {category['name']}")  # Display clean category name
            print()
            choice = input(PromptHelper.choose_option()).strip()
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(sorted_categories):
                    return sorted_categories[index]['name']  # Return clean category name
                else:
                    print()
                    print(PromptHelper.invalid_input())
                    print()
                    input(PromptHelper.enter_try_again())
                    continue
            except ValueError:
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
                continue