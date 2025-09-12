from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.scrollview import ScrollView
from widgets.appointment_card import AppointmentCard


class StartScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # überschrift
        self.add_widget(MDLabel(text="♡ Meine Termine ♡", halign="center"))

        # Scrollbarer Bereich
        scroll = ScrollView(size_hint=(1, 0.85))
        self.layout = MDBoxLayout(
            orientation = "vertical",
            spacing = 10,
            padding = 20,
            size_hint_y = None
        )
        self.layout.bind(minimum_height=self.layout.setter("height"))
        scroll.add_widget(self.layout)
        self.add_widget(scroll)

        # Button unten
        new_btn = MDRaisedButton(
            text = "Neuen Termin hinzufügen",
            pos_hint = {"center_x": 0.5, "center_y": 0.05},
            on_release=self.goto_add
        )
        self.add_widget(new_btn)

    def add_appointment(self, appointment):
        card = AppointmentCard(appointment)
        self.layout.add_widget(card)

    def goto_add(self, instance):
        self.manager.current = "add"
