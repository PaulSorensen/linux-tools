from controller.generate.markdown_generator import MarkdownGenerator
from controller.generate.yaml_generator import YamlGenerator
from controller.generate.json_generator import JsonGenerator
from controller.generate.text_generator import TextGenerator
from helper.layout_helper import LayoutHelper
from helper.prompt_helper import PromptHelper

class GenerateController:
    """Controller for generate output menu operations."""

    generators = [
        ("Markdown", MarkdownGenerator),
        ("Text", TextGenerator),
        ("JSON", JsonGenerator),
        ("YAML", YamlGenerator),
    ]

    def run(self):
        """Display generate output menu and handle selection."""
        while True:
            LayoutHelper.clear()
            LayoutHelper.header()
            print("1) Generate Markdown")
            print("2) Generate Text")
            print("3) Generate JSON")
            print("4) Generate YAML")
            print("5) Generate all")
            print("0) Back to Main Menu")
            print()
            choice = input(PromptHelper.choose_option()).strip()
            print()

            if choice in {"1", "2", "3", "4"}:
                idx = int(choice) - 1
                gen_name, gen_class = self.generators[idx]
                gen_class().generate()
                LayoutHelper.clear()
                LayoutHelper.header()
                print(f"{gen_name} generated: {gen_class.filename}")
                print()
                input(PromptHelper.enter_main_menu())
                break
            elif choice == "5":
                for gen_name, gen_class in self.generators:
                    gen_class().generate()
                LayoutHelper.clear()
                LayoutHelper.header()
                print("All formats generated:")
                for gen_name, gen_class in self.generators:
                    print(f"- {gen_name}: {gen_class.filename}")
                print()
                input(PromptHelper.enter_main_menu())
                break
            elif choice == "0":
                break
            else:
                print(PromptHelper.invalid_input())
                print()
                input(PromptHelper.enter_try_again())
                LayoutHelper.clear()
                LayoutHelper.header()