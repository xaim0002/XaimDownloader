[app]

title = Xaim Downloader

package.name = xaimdownloader

package.domain = com.xaimtech

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

version = 1.0

requirements = python3,kivy,yt-dlp,certifi,urllib3,idna,charset-normalizer

orientation = portrait

fullscreen = 1

android.api = 33

android.build_tools_version = 33.0.2

android.minapi = 21

android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET

android.private_storage = True


[buildozer]

log_level = 2

warn_on_root = 1