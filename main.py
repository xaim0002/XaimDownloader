import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image as KivyImage
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.progressbar import ProgressBar
import yt_dlp

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
        
        # 4. Format Selection
        self.format_spinner = Spinner(
            text='Quality Select Karein',
            values=('Best Video (MP4)', 'Audio Only (MP3)'),
            size_hint_y=None, height=50
        )
        layout.add_widget(self.format_spinner)
        
        # 5. Progress Section
        self.status_label = Label(text="Status: Ready", font_size='14sp')
        layout.add_widget(self.status_label)
        
        self.progress_bar = ProgressBar(max=100, size_hint_y=None, height=20)
        layout.add_widget(self.progress_bar)
        
        # 6. Download Button
        btn = Button(text="⚡ Download Start", background_color=(0.18, 0.49, 0.20, 1), font_size='18sp', bold=True, size_hint_y=None, height=55)
        btn.bind(on_press=self.start_download_thread)
        layout.add_widget(btn)
        
        # 7. Footer
        layout.add_widget(Label(text=f"Developed by: {self.developer}", font_size='11sp', color=(0.5, 0.5, 0.5, 1)))
        
        return layout

    def start_download_thread(self, instance):
        threading.Thread(target=self.download_process, daemon=True).start()

    def download_hook(self, d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate') or 0
            downloaded = d.get('downloaded_bytes', 0)
            if total > 0:
                percent = int((downloaded / total) * 100)
                self.progress_bar.value = percent
                self.status_label.text = f"Downloading: {percent}%"
        elif d['status'] == 'finished':
            self.status_label.text = "✅ Download Mukammal! Saved to Downloads."

    def download_process(self):
        url = self.url_input.text
        fmt = self.format_spinner.text
        
        if not url or fmt == 'Quality Select Karein':
            self.status_label.text = "❌ Error: Link ya Format missing hai!"
            return
            
        self.status_label.text = "Fetching & Starting Download..."
        self.url_input.text = ""  # Input box instantly empty ho jaye ga
        
        # Android path configuration
        download_folder = '/sdcard/Download'
        
        ydl_opts = {
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'progress_hooks': [self.download_hook],
        }
        
        if fmt == 'Audio Only (MP3)':
            ydl_opts['format'] = 'bestaudio'
        else:
            ydl_opts['format'] = 'best'
            
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            self.status_label.text = f"❌ Error: Kuch ghalat hua!"

if __name__ == '__main__':
    XaimDownloaderApp().run()
