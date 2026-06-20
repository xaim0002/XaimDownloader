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
        
        # Main Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=12)
        
        # 1. Logo Section
        if os.path.exists('logo.png'):
            layout.add_widget(KivyImage(source='logo.png', size_hint=(1, 0.2)))
            
        # 2. Header Branding
        layout.add_widget(Label(text=self.brand_name, font_size='26sp', bold=True, color=(0.12, 0.41, 0.64, 1)))
        layout.add_widget(Label(text=self.tagline, font_size='14sp', italic=True, color=(0.6, 0.6, 0.6, 1), size_hint_y=None, height=20))
        
        # 3. Input Box
        self.url_input = TextInput(hint_text="Video ka link yahan paste karein...", multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.url_input)
        
        # 4. Status
        self.status_label = Label(text="Status: Ready", font_size='14sp')
        layout.add_widget(self.status_label)
        
        self.progress_bar = ProgressBar(max=100, size_hint_y=None, height=20)
        layout.add_widget(self.progress_bar)
        
        # 5. Download Button
        btn = Button(text="⚡ Download Start", background_color=(0.18, 0.49, 0.20, 1), font_size='18sp', bold=True, size_hint_y=None, height=55)
        layout.add_widget(btn)
        
        # 6. Footer
        layout.add_widget(Label(text=f"Developed by: {self.developer}", font_size='11sp', color=(0.5, 0.5, 0.5, 1)))
        
        return layout

if __name__ == '__main__':
    XaimDownloaderApp().run()
