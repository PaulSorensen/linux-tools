#!/usr/bin/env python3
"""
################################################################################
 Linux Tools CLI Application
################################################################################
 Author        : Paul Sørensen
 Website       : https://paulsorensen.io
 GitHub        : https://github.com/paulsorensen
 Version       : 1.0
 Last Modified : 2025/06/02 22:56:48

 Description:
 MVC-structured CLI application for managing a Linux Tools database,
 and generating structured output in various formats.
 Provides add, delete, order, and output generation features.
 Uses YAML for data storage.
 
 Usage: Run 'run.sh' to launch the interactive CLI.
        See README.md for full documentation and usage.

 If you found this project useful, a small tip is appreciated ❤️
 https://buymeacoffee.com/paulsorensen
################################################################################
"""

import sys
import yaml
from pathlib import Path
from controller.add_controller import AddController
from controller.delete_controller import DeleteController  
from controller.order_controller import OrderController
from controller.generate_controller import GenerateController
from helper.layout_helper import LayoutHelper
from helper.prompt_helper import PromptHelper

# Add project root to path for imports
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

class LinuxToolsApp:
    """Main application controller"""
    
    def __init__(self):
        """Initialize the application"""
        self.setup_data_directory()
        
    def setup_data_directory(self):
        """Ensure data directory and files exist"""
        data_path = Path("data")
        data_path.mkdir(exist_ok=True)
        
        # Initialize YAML files if they don't exist
        files = {
            "structure.yaml": {},
            "tools.yaml": []
        }
        
        for filename, default_content in files.items():
            file_path = data_path / filename
            if not file_path.exists():
                with open(file_path, 'w') as f:
                    yaml.dump(default_content, f, default_flow_style=False)
    
    def print_menu(self):
        print("1) Add")
        print("2) Delete")
        print("3) Manage Order")
        print("4) Generate Output")
        print("0) Exit")
        print()
    
    def run(self):
        """Display main menu and handle selecion"""
        while True:
            LayoutHelper.clear()
            LayoutHelper.header()
            
            self.print_menu()
            choice = input(PromptHelper.choose_option()).strip()
            
            if choice == "1":
                AddController().run()
            elif choice == "2":
                DeleteController().run()
            elif choice == "3":
                OrderController().run()
            elif choice == "4":
                GenerateController().run()
            elif choice == "0":
                print("\nGoodbye!")
                sys.exit(0)
            else:
                print()
                print(PromptHelper.invalid_input())
                input(PromptHelper.enter_try_again())

if __name__ == "__main__":
    app = LinuxToolsApp()
    app.run()