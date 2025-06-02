import os

class LayoutHelper:
    """Helper for managing and formatting layout"""

    @staticmethod
    def clear():
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def app_name():
        """Returns the name of the application."""
        return "🐧 Linux Tools"

    @staticmethod
    def header():
        """Display application header."""
        print(LayoutHelper.app_name())
        print("© 2005 Paul Sørensen")
        print()