from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

class StartScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
# **kwargs - keyword arguments
# nimmt beliebe Anzahl an Argumeneten an
# sammelt alle übergebenen Parameter in einem Dictionary(z.B name=wert, alter=wert...)

        # Überschrift
        self.add_widget(MDLabel(text = "♡ Meine Termine ♡", halign = "center"))

        # button zum add_screen
        add_btn = MDRaisedButton(
            text = "Neuen Termin hinzufügen",
            pos_hint = {"center_x": 0.5, "center_y": 0.3},
            on_release = self.goto_add
        )
        self.add_widget(add_btn)

    def goto_add(self, _):
        # wechselt zu screen add
        self.manager.current = "add"