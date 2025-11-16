"""
CP1404 - Practical 08
Mile to Km converter.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_FACTOR = 1.60934

class MilesConverterApp(App):
    """A Kivy app to convert miles to km."""

    km_result = StringProperty()

    def build(self):
        """Build Kivy app from kv file."""
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, text, change):
        """Update the text with the change added."""
        miles = self.convert_text_to_float(text) + change
        self.root.ids.input_miles.text = str(miles)

    def handle_conversion(self, text):
        """Handle the conversion of miles to km."""
        miles = self.convert_text_to_float(text)
        self.update_result(miles)

    def update_result(self, miles):
        """Update the result with the output of the calculation."""
        self.km_result = str(miles * MILES_TO_KM_FACTOR)

    def convert_text_to_float(self, text):
        """Convert text to float, return 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0

MilesConverterApp().run()