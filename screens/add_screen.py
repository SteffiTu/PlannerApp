from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from datetime import datetime


class AddScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Titel
        self.title_input = MDTextField(
            hint_text="Titel des Termins",
            pos_hint={"center_x": 0.5, "center_y": 0.75},
            size_hint_x=0.8
        )
        self.add_widget(self.title_input)

        #Notiz
        self.note_input = MDTextFieldRect(
            hint_text="Notiz (optional)",
            pos_hint={"center_x": 0.5, "center_y": 0.63},
            size_hint=(0.8, 0.1)
        )
        self.add_widget(self.note_input)

        #Datum Button
        self.date_btn = MDRaisedButton(
            text="Datum wählen",
            pos_hint={"center_x": 0.5, "center_y": 0.52},
            on_release=self.show_date_picker
        )
        self.add_widget(self.date_btn)

        #Uhrzeit Textfeld
        self.time_input = MDTextField(
            hint_text="Uhrzeit (HH:MM)",
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            size_hint_x=0.4
        )
        self.add_widget(self.time_input)

        #Anzeige Label
        self.info_label = MDLabel(
            text="Noch kein Datum/Uhrzeit ausgewählt",
            halign="center",
            pos_hint={"center_y": 0.38}
        )
        self.add_widget(self.info_label)

        #Speichern Button
        save_btn = MDRaisedButton(
            text="Speichern",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_release=self.save_appointment
        )
        self.add_widget(save_btn)

        #Zurück Button
        back_btn = MDRaisedButton(
            text="Zurück",
            pos_hint={"center_x": 0.5, "center_y": 0.22},
            on_release=self.goto_start
        )
        self.add_widget(back_btn)

        # Variablen
        self.selected_date = None

    #Datum Picker
    def show_date_picker(self, instance):
        from kivymd.uix.pickers import MDDatePicker
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_selected)
        date_dialog.open()

    def on_date_selected(self, instance, value, date_range):
        self.selected_date = value
        self.update_label()

    #Label aktualisieren
    def update_label(self):
        date_text = self.selected_date.strftime("%d.%m.%Y") if self.selected_date else ""
        time_text = self.time_input.text.strip()
        if date_text and time_text:
            self.info_label.text = f"Gewählt: {date_text} - {time_text}"
        elif date_text:
            self.info_label.text = f"Datum: {date_text}"
        elif time_text:
            self.info_label.text = f"Uhrzeit: {time_text}"
        else:
            self.info_label.text = "Noch kein Datum/Uhrzeit ausgewählt"

    #Speichern
    def save_appointment(self, instance):
        title = self.title_input.text.strip()
        note = self.note_input.text.strip()
        time_text = self.time_input.text.strip()

        if not title:
            self.info_label.text = "Bitte einen Titel eingeben"
            return
        if not self.selected_date or not time_text:
            self.info_label.text = "Bitte Datum und Uhrzeit auswählen"
            return

        # eingegebene Uhrzeit verarbeiten
        try:
            hour, minute = map(int, time_text.split(":"))
            selected_time = datetime.strptime(f"{hour}:{minute}", "%H:%M").time()
        except ValueError:
            self.info_label.text = "Uhrzeit ungültig, Format HH:MM"
            return

        # Termin-Objekt erstellen
        appointment = {
            "title": title,
            "note": note,
            "datetime": datetime.combine(self.selected_date, selected_time)
        }

        # An StartScreen übergeben
        self.manager.get_screen("start").add_appointment(appointment)
        self.manager.current = "start"

    #Zurück
    def goto_start(self, instance):
        self.manager.current = "start"