from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from utils.date_utils import countdown_text


class AppointmentCard(MDCard):
    def __init__(self, appointment, **kwargs):
        super().__init__(
            orientation = "vertical",
            size_hint = (0.9, None),
            height = 150,
            padding = 15,
            radius = [20],
            md_bg_color = (1, 0.9, 1, 1),
            pos_hint = {"center_x": 0.5},
            **kwargs
        )

        # Titel
        self.add_widget(MDLabel(
            text = f"{appointment['title']}",
            halign = "left",
            theme_text_color = "Primary"
        ))

        # Notiz
        if appointment["note"]:
            self.add_widget(MDLabel(
                text = f"{appointment['note']}",
                halign = "left",
                theme_text_color = "Secondary"
            ))

        # Datum
        self.add_widget(MDLabel(
            text = appointment["datetime"].strftime("%d.%m.%Y %H:%M"),
            halign = "left",
            theme_text_color = "Secondary"
        ))

        # Countdown
        self.add_widget(MDLabel(
            text = f"{countdown_text(appointment['datetime'])}",
            halign = "left",
            theme_text_color = "Error"
        ))
