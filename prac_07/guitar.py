"""
CP1404 - Practical 07
Guitar class file.
"""


class Guitar:
    """Guitar class to store details for a guitar."""
    CURRENT_YEAR = 2022

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string format of guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate age of guitar."""
        return self.CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage (age >= 50 years)."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Is the guitar older than the other guitar."""
        return self.year < other.year
