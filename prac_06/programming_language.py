"""
CP1404 - Practical 06
Programming languages class file.
Estimate: 80 minutes
Actual:
"""


class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=False, year=""):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Is the language's typing dynamic."""
        if self.typing == "Dynamic":
            return True
        return False
