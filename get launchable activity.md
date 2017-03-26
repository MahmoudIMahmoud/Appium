# How to get launchable activity name of package from adb?
### If you have the .apk <br>
```shell
Windows cmd:
aapt dump badging <the app file.apk> | findstr launchable-activity
Linux:
aapt dump badging <the app file.apk> | grep launchable-activity
```
### If you don't have the .APK file.<BR>
```shell
Get the path of the apk on the device.
adb shell pm list packages -f | findstr <any part of package you may know>
adb pull <APK path from previous command>
```
### Another way using ADB.<BR>
Given that the app you are aiming to get its info is running in the front of the mobile focus.<br>
```shell
adb shell dumpsys window windows | findstr Focus
```
