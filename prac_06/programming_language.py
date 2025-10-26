"""
CP1404 - Practical 06
Programming languages class file.
Estimate: 80 minutes
Actual:
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string format of programming language object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if the language is dynamically typed."""
        return self.typing == "Dynamic"

