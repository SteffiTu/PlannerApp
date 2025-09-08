from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

class AddScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(MDLabel(text = "Termin hinzufügen", halign = "center"))

        back_btn = MDRaisedButton(
            text = "zurück",
            pos_hint = {"center_x": 0.5, "center_y": 0.3},
            on_release = self.goto_start
        )
        self.add_widget(back_btn)

    def goto_start(self, _):
        # wechselt zu screen start
        self.manager.current = "start"