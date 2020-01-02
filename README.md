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
* This SDK works with Rakuten ID SDK

| Version        | Minimum OS           | Compile OS
--- | --- | ---
|0.1.0|16(4.1)|28 (9.0)|

* Developers can ingegrate SDK 4.x but SDK function does not work under Android 5

<div id="import_sdk"></div>

## Import the Reward SDK
Apps can import Reward SDK modules with a Gradle dependency. In order to use that repository, you need to reference it int the app's project-level `build.gradle` file. Open yours and look for an allprojects section:  

**Example project-level build.gradle**

```groovy

allprojects {
    repositories {
        jcenter()
        maven {
            url "https://github.com/rakuten-ads/rakuten-ads-android/raw/master/maven"
        }
        maven { 
            url 'https://raw.github.com/rakuten-ads/rakuten-ads-android/master/maven' 
        }
    }
}
```

Next, open the app-level `build.gradle` file for your app, and look for a "dependencies" section.

```groovy
  implementation 'com.rakuten.android.ads:rewardsdknative:0.1.0'
```

## Usage
[Basic Guide](./doc/basic/README.md)  
[Advanced Guide](./doc/advanced/README.md)

## Proguard Setting
To keep API (not to obfuscate codes), add following description
```
############ Reward SDK ##################
-keepattributes *Annotation*
-keepattributes Signature
-keep class com.rakuten.android.ads.core.** { *; }
-keep class com.rakuten.gap.ads.rakutenrewardnative.ui.** { *; }
-keep class com.rakuten.gap.ads.rakutenrewardnative.api.** { *; }
-keep public enum com.rakuten.gap.ads.rakutenrewardnative.api.status.** {
 **[] $VALUES;
 public *;
}
```

---
LANGUAGE :
> [![jp](./doc/lang/ja.png)](./doc/ja/README.md)



