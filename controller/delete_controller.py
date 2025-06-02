from controller.section_controller import SectionController
from controller.category_controller import CategoryController
from controller.tool_controller import ToolController
from helper.layout_helper import LayoutHelper
from helper.prompt_helper import PromptHelper

class DeleteController:
    """Controller for delete menu operations."""
    
    def run(self):
        """Display delete menu and handle selection."""
        while True:
            LayoutHelper.clear()
            LayoutHelper.header()
            
            print("1) Delete Section")
            print("2) Delete Category")
            print("3) Delete Tool") 
            print("0) Back to Main Menu")
            print()
            
            choice = input(PromptHelper.choose_option()).strip()
            
            if choice == "1":
                SectionController().delete()
                break
            elif choice == "2":
                CategoryController().delete()
                break
            elif choice == "3":
                ToolController().delete()
                break
            elif choice == "0":
                break
            else:
                print()
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())