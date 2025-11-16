"""
CP1404 - Practical 08
Dynamic Labels File.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def build(self):
        """Build the kivy GUI."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels for each name in list."""
        names = ["Camilla", "Jonny", "Brain", "Tim"]
        for name in names:
            name_label = Label(text=name)
            self.root.ids.main.add_widget(name_label)


DynamicLabelsApp().run()
