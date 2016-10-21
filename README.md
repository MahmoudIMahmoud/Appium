# AppiumPythonTut
##Code Changes:

```python
        desired_caps = {'platformName': "Android", 'deviceName': "<Your device here>",
                        'app':os.path.abspath("./Apps/app-debug.apk")}
```
##Get your device name:
###On the command run:
```bat
        adb devices
```
##Settings:
-   Open Appium (server)
-   In the adroid settings:
    -   Clear all the check boxes.
    -   Install the app on the mobile/emulator.
    ![](https://github.com/MahmoudIMahmoud/AppiumPythonTut/blob/master/Untitled.jpg)
