import os
import re
class DataHelper:
    """Helper for data normalization and transformation."""

    @staticmethod
    def load_acronyms():
        """Load and normalize acronyms from a file."""

        file_path = os.path.join(os.path.dirname(__file__), "../data/acronyms.txt")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return sorted([
                    line.strip() for line in f.readlines()
                    if line.strip()
                ])
        except FileNotFoundError:
            return []    
    
    @staticmethod
    def title_case(text):
        """Convert text to title case with acronym preservation."""
        minor_words = {"and", "or", "the", "a", "an", "in", "on", "with", "to", "of", "at", "by", "for"}
        acronyms = DataHelper.load_acronyms()
        words = text.split()

        result = []
        for i, word in enumerate(words):
            match = next((a for a in acronyms if a.lower() == word.lower()), None)
            if match:
                result.append(match)
            elif i == 0 or i == len(words) - 1 or word.lower() not in minor_words:
                result.append(word.capitalize())
            else:
                result.append(word.lower())

        return " ".join(result)
    
    @staticmethod
    def capitalize_first(text):
        """Capitalize first word of the text."""
        return text[:1].upper() + text[1:] if text else ""
    
    @staticmethod
    def sanitize(prompt: str):
        """Remove all special characters, keeping only letters and numbers."""
        return re.sub(r'[^a-zA-Z0-9 ]+', '', prompt)    