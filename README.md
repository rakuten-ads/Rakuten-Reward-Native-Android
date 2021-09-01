<div id="top"></div>

[![Platform](http://img.shields.io/badge/platform-Android-brightgreen.svg?style=flat)](https://developer.android.com)
[![Language](http://img.shields.io/badge/language-Kotlin-green.svg?style=flat)](https://github.com/JetBrains/kotlin)
[![Android](http://img.shields.io/badge/support-API_Level_16+-blue.svg?style=flat)](https://developer.android.com)

# Rakuten Reward SDK Native

---
# Get Started

<div id="prerequisites"></div>

## Prerequisites

* Use Android Studio 1.0 or higher
* Target Android API level 16 or higher
* Support Android X
* Use Rakuten IDSDK or Use built-in Login

| Version        | Minimum SDK           | Compile SDK
--- | --- | ---
|1.0.0|API16 (4.1)|API 29|
|1.1.0|API16 (4.1)|API 29|
|1.1.1|API16 (4.1)|API 29|
|1.1.2|API16 (4.1)|API 29|
|1.1.3|API16 (4.1)|API 29|
|2.0.0|API16 (4.1)|API 29|
|2.1.0|API16 (4.1)|API 29|
|2.2.0|API16 (4.1)|API 29|
|2.2.1|API16 (4.1)|API 29|
|2.2.2|API16 (4.1)|API 29|

* SDK functions only work with API 21 and above

<div id="import_sdk"></div>

## Import the Reward SDK
Apps can import Reward SDK modules with a Gradle dependency. In order to use that repository, you need to reference it int the app's project-level `build.gradle` file. Open yours and look for an allprojects section:  

**Example project-level build.gradle**

```groovy

allprojects {
    repositories {
        jcenter()
        maven { 
            url 'https://raw.github.com/rakuten-ads/rakuten-ads-android/master/maven' 
        }
        maven {
            url "https://raw.github.com/rakuten-ads/Rakuten-Reward-Native-Android/master/maven"
        }
    }
}
```

Next, open the app-level `build.gradle` file for your app, and look for a "dependencies" section.

```groovy
  implementation 'com.rakuten.android:rewardsdknative-ui:2.2.2'
```
If you don't use our built-in ui, you can skip "rewardsdknative-ui"
```groovy
  implementation 'com.rakuten.android:rewardsdknative-core:2.2.2'
```
※ rewardsdknative-ui module uses viewbinding and databinding.  
If your app does not use both, please add following to build.gradle
```groovy
buildFeatures {
        viewBinding true
        dataBinding true
}
```
※ And if your app supports under Android 5, add vectorDrawable support (Can integrate Android 4 but all functions are available over Android 5)
```groovy
vectorDrawables.useSupportLibrary = true
```

If you need to use under 2.0.0, Plesae use following
```groovy
  implementation 'com.rakuten.android:rewardsdknative:1.1.3'
```

## Usage
[Basic Guide](./doc/basic/README.md)  
[API Reference](./doc/APIReference/README.md)

## Version History
[Version History](./doc/history/README.md)

---
LANGUAGE :
> [![jp](./doc/lang/ja.png)](./doc/ja/README.md)
