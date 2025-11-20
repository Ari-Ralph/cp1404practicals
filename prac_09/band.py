"""
CP1404 - Practical 09
Band class.
"""


class Band:
    """Band class containing musicians."""

    def __init__(self, name):
        """Initialise a Band object with a musician list"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string format of band instance."""
        return f"{self.name} ({", ".join([str(musician) for musician in self.musicians])})"

    def add(self, musician):
        """Append item to musician list."""
        self.musicians.append(musician)

    def play(self):
        """Return a string of all musicians playing."""
        return "\n".join([musician.play() for musician in self.musicians])
