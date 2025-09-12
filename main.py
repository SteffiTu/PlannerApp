from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from screens.start_screen import StartScreen
from screens.add_screen import AddScreen


class MagicalPlannerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.theme_style = "Light"

        sm = ScreenManager()
        sm.add_widget(StartScreen(name = "start"))
        sm.add_widget(AddScreen(name = "add"))
        return sm
# cls - Abkürzung für class,
# dient als PLatzhalter für "die Klasse, die gerade arbeitet"

if __name__ == "__main__":
    MagicalPlannerApp().run()