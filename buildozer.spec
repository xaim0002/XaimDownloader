[app]
# (string) Title of your application
title = Xaim Downloader

# (string) Package name
package.name = xaimdownloader

# (string) Package domain (needed for android package name)
package.domain = com.xaimtech

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (string) Application versioning
version = 1.0

# (list) Application requirements
# Crucial: We need python3, kivy, and yt-dlp library
requirements = python3,kivy,yt-dlp,certifi,urllib3,idna,charset-normalizer

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use private storage for data
android.private_storage = True

# (str) Title of the screen orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
