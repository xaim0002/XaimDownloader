import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image as KivyImage
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar


class XaimDownloaderApp(App):

    def build(self):

        self.brand_name = "Xaim Technologies"
        self.tagline = "Building Ideas into reality"
        self.developer = "Aamir Xaim"


        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )


        if os.path.exists("logo.png"):
            layout.add_widget(
                KivyImage(
                    source="logo.png",
                    size_hint=(1,0.2)
                )
            )


        layout.add_widget(
            Label(
                text=self.brand_name,
                font_size="26sp"
            )
        )


        layout.add_widget(
            Label(
                text=self.tagline,
                font_size="14sp"
            )
        )


        self.url_input = TextInput(
            hint_text="Video link paste karein...",
            multiline=False,
            size_hint_y=None,
            height=50
        )

        layout.add_widget(self.url_input)



        self.status_label = Label(
            text="Status: Ready"
        )

        layout.add_widget(self.status_label)



        self.progress_bar = ProgressBar(
            max=100,
            size_hint_y=None,
            height=20
        )

        layout.add_widget(self.progress_bar)



        btn = Button(
            text="⚡ Download Start",
            size_hint_y=None,
            height=55
        )

        btn.bind(
            on_press=self.start_download
        )

        layout.add_widget(btn)



        layout.add_widget(
            Label(
                text=f"Developed by: {self.developer}"
            )
        )


        return layout



    def start_download(self, instance):

        url = self.url_input.text

        if url:

            self.status_label.text = "Status: Download started"

        else:

            self.status_label.text = "Please enter link"



if __name__ == "__main__":
    XaimDownloaderApp().run()