# ImageRecognitionAPK
Image Recognition for android, and next step, it will be trained to recognize the pictures you upload


## Build step
1. install kivy
pip install kivy, pyobjus, kivymd
2. install buildozer
pip install buildozer
3. buildozer init
in your cmd input: buildozer init
it will create a file named `buildozer.spec`
4. config the `buildozer.spec`
5. build the apk
buildozer -v android debug

## Common Mistakes
# 1. This buildozer version requires a python-for-android version with AAB (Android App Bundle) support. Please update your pinned version accordingly.
find a line of `#p4a.branch = master` in your `buildozer.spec`, and change it to `p4a.branch = develop`
than call `buildozer android clean` after that call `buildozer -v android debug`
