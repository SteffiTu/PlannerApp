from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout


class PlannerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.theme_style = "Light"

        # Beispiel-Termine (später dynamisch speicherbar)
        self.termin_liste = [
            {"titel": "🎀 Zahnarzttermin", "datum": "05.09.2025 - 14:30 Uhr", "countdown": "Noch 3 Tage"},
            {"titel": "🌸 Treffen mit Anna", "datum": "06.09.2025 - 18:00 Uhr", "countdown": "Noch 4 Tage"},
            {"titel": "✨ Projekt-Abgabe", "datum": "10.09.2025 - 12:00 Uhr", "countdown": "Noch 8 Tage"},
            {"titel": " Zertifikat Scrum", "datum": "6.09.2025 - 11:00 Uhr", "countdown": "Noch 1 Tage"},
        ]

        main_layout = MDBoxLayout(orientation="vertical", spacing=10, padding=10)

        # Überschrift
        main_layout.add_widget(
            MDLabel(
                text="♡ My Planner ♡",
                halign="center",
                theme_text_color="Primary",
                font_style="H4"
            )
        )

        # Dynamisch Karten für jeden Termin erstellen
        for termin in self.termin_liste:
            card = self.erzeuge_termin_karte(termin)
            main_layout.add_widget(card)

        # Button zum Hinzufügen neuer Termine
        main_layout.add_widget(
            MDRectangleFlatButton(
                text="➕ Neuen Termin hinzufügen",
                pos_hint={"center_x": 0.5},
                on_release=lambda x: print("Neuen Termin hinzufügen gedrückt!")
            )
        )

        screen = Screen()
        screen.add_widget(main_layout)
        return screen

    def erzeuge_termin_karte(self, termin):
        """Erzeugt eine MDCard für einen Termin."""
        card = MDCard(
            orientation="vertical",
            size_hint=(1, None),
            height=180,
            padding=15,
            md_bg_color=(1, 0.9, 1, 1),
            style="elevated"
        )

        card.add_widget(MDLabel(text=termin["titel"], theme_text_color="Primary", font_style="H6"))
        card.add_widget(MDLabel(text=f"📅 Datum: {termin['datum']}", theme_text_color="Secondary"))
        card.add_widget(MDLabel(text=f"⏳ {termin['countdown']}", theme_text_color="Secondary"))

        # Bearbeiten-Button
        card.add_widget(
            MDRaisedButton(
                text="Bearbeiten",
                pos_hint={"center_x": 0.5},
                on_release=lambda x: print(f"Bearbeite {termin['titel']}")
            )
        )
        return card


PlannerApp().run()
