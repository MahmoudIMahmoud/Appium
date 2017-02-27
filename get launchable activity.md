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
