"""
CP1404 - Practical 06
Guitar class file.
Estimate: 40 minutes
Actual:
"""

CURRENT_YEAR = 2022


class Guitar:
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
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage (age >= 50 years)."""
        return self.get_age() >= 50
