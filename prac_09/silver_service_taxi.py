"""
CP1404 - Practical 09
Silver Service Car class.
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with fanciness pricing and additional fees."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi, with parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return price of fare with flagfall."""
        return self.flagfall + super().get_fare()