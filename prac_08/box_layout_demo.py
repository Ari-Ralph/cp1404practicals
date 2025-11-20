"""
CP1404 - Practical 08
Box layout console file.
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Create a GUI that can manipulate user input."""

    def build(self):
        """Build object layout."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Print greeting using input name."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear the input name and output label."""
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
