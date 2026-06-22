[app]

title = Xaim Downloader
package.name = xaimdownloader
package.domain = com.xaimtech

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

version = 1.0

requirements = python3,kivy==2.3.0,yt-dlp,certifi,urllib3,idna,charset-normalizer

orientation = portrait
fullscreen = 1

android.minapi = 21
android.api = 33

android.permissions = INTERNET

android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1