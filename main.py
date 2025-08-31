from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton



class MyApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation = "vertical", 
                           spacing = 10, 
                           padding = 20,
                           )

        layout.add_widget(MDLabel(text = "Hallo!", 
                                halign = "center",
                                theme_text_color="Custom",
                                text_color=(1, 0.5, 1, 1),
                                font_style="H4"
                                ))
        
        layout.add_widget(MDRaisedButton(text = "Drück mich!", 
                                        on_release = lambda x: print("click!"),
                                        pos_hint={"center_x": 0.5, "center_y": 0.5}, 
                                        theme_text_color="Custom", 
                                        text_color=(1,0.5, 1, 1)
                                        ))
        
        layout.add_widget(MDTextField(hint_text="Gib hier etwas ein...",
                                    pos_hint={"center_x": 0.5, "center_y": 0.6},
                                    size_hint_x=None,
                                    width=200
                                    ))
        
        layout.add_widget(MDCard(size_hint=(0.6, 0.2),
                                pos_hint={"center_x": 0.5, "center_y": 0.4},
                                elevation=8,    # Schatten
                                radius=[20,],    # abgerundete Ecken
                                ))
        
        layout.add_widget(MDIconButton(icon="heart",    # Emoji/Material-Icon
                                    pos_hint={"center_x": 0.8, "center_y": 0.8},
                                    on_release=lambda x: print("Herz gedrückt!"),
                                    theme_text_color="Custom",
                                    text_color=(1,0.5, 1, 1)
                                    ))

        return layout

MyApp().run()
