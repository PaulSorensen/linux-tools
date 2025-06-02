class PromptHelper:
    """Helper for reusable CLI output strings."""

    @staticmethod
    def choose_option():
        """Return prompt for choosing an option."""
        return "Choose an option: "
    
    @staticmethod
    def invalid_input():
        """Return prompt for invalid input."""
        return "Invalid input!"
    
    @staticmethod
    def enter_try_again():
        """Return prompt for try again."""
        return "Press Enter to try again..."

    @staticmethod
    def enter_continue():
        """Return prompt for continue."""
        return "Press Enter to continue..."

    @staticmethod
    def enter_main_menu():
        """Return prompt for returning to main menu."""
        return "Press Enter to return to Main Menu..."