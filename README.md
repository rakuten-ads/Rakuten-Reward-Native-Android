<div id="top"></div>

[![Platform](http://img.shields.io/badge/platform-Android-brightgreen.svg?style=flat)](https://developer.android.com)
[![Language](http://img.shields.io/badge/language-Kotlin-green.svg?style=flat)](https://github.com/JetBrains/kotlin)
[![Android](http://img.shields.io/badge/support-API_Level_24+-blue.svg?style=flat)](https://developer.android.com)

# Rakuten Reward SDK Native

---
# Get Started

<div id="prerequisites"></div>

## Prerequisites

* Use Android Studio Arctic Fox or higher
* Target Android API level 24 or higher
* Support Android X
* Use Rakuten IDSDK or Use built-in Login

| Version | Minimum SDK | Compile SDK |
|---------|-------------|-------------|
| 5.1.0   | API24 (7.0) | API 34      |
| 5.0.0   | API24 (7.0) | API 34      |
| 4.1.0   | API24 (7.0) | API 33      |
| 4.0.0   | API21 (5.0) | API 33      |
| 3.7.0   | API21 (5.0) | API 33      |
| 3.6.0   | API21 (5.0) | API 33      |
| 3.5.1   | API21 (5.0) | API 33      |
| 3.5.0   | API21 (5.0) | API 33      |

<details>
    <summary>Older Verions</summary>

| Version | Minimum SDK | Compile SDK |
|---------|-------------|-------------|
| 3.4.2   | API21 (5.0) | API 33      |
| 3.4.1   | API21 (5.0) | API 33      |
| 3.4.0   | API21 (5.0) | API 31      |
| 3.3.0   | API21 (5.0) | API 30      |
| 3.2.2   | API21 (5.0) | API 30      |
| 3.2.1   | API21 (5.0) | API 30      |
| 3.2.0   | API21 (5.0) | API 30      |
| 3.1.2   | API21 (5.0) | API 30      |
| 3.1.1   | API21 (5.0) | API 30      |
| 3.1.0   | API21 (5.0) | API 30      |
| 3.0.0   | API21 (5.0) | API 30      |
| 1.1.4   | API16 (4.1) | API 30      |
| 2.4.1   | API16 (4.1) | API 30      |
| 2.4.0   | API16 (4.1) | API 30      |
| 2.3.3   | API16 (4.1) | API 29      |
| 2.3.2   | API16 (4.1) | API 29      |
| 2.3.1   | API16 (4.1) | API 29      |
| 2.3.0   | API16 (4.1) | API 29      |
| 2.2.2   | API16 (4.1) | API 29      |
| 2.2.1   | API16 (4.1) | API 29      |
| 2.2.0   | API16 (4.1) | API 29      |
| 2.1.0   | API16 (4.1) | API 29      |
| 2.0.0   | API16 (4.1) | API 29      |
| 1.1.3   | API16 (4.1) | API 29      |
| 1.1.2   | API16 (4.1) | API 29      |
| 1.1.1   | API16 (4.1) | API 29      |
| 1.1.0   | API16 (4.1) | API 29      |
| 1.0.0   | API16 (4.1) | API 29      |

</details>

<div id="import_sdk"></div>

## Import the Reward SDK
Apps can import Reward SDK modules with a Gradle dependency. In order to use that repository, you need to reference it int the app's project-level `build.gradle` file. Open yours and look for an allprojects section:  

**Example project-level build.gradle**

```groovy

allprojects {
    repositories {
        mavenCentral()
        maven {
            url "https://raw.github.com/rakuten-ads/Rakuten-Reward-Native-Android/master/maven"
        }
    }
}
```

Next, open the app-level `build.gradle` file for your app, and look for a "dependencies" section.

```groovy
  implementation 'com.rakuten.android:rewardsdknative-ui:5.1.0'
```
If you don't use our built-in ui, you can skip "rewardsdknative-ui"
```groovy
  implementation 'com.rakuten.android:rewardsdknative-core:5.1.0'
```
※ rewardsdknative-ui module uses viewbinding and databinding.  
If your app does not use both, please add following to build.gradle
```groovy
buildFeatures {
        viewBinding true
        dataBinding true
}
```

If you need to use under 2.0.0, Plesae use following
```groovy
  implementation 'com.rakuten.android:rewardsdknative:1.1.4'
```

# Android Gradle Plugin 7.0
Since version 3.6.0, Reward SDK modules has upgrade Android Gradle Plugin (AGP) to version 7.1.  
Please upgrade your application's AGP to version 7.0 or later.
```groovy
dependencies {
    classpath "com.android.tools.build:gradle:7.0.3"
}
```

# User Consent 
Since version 4.0.0, end users have to provide consent for Reward terms of use and privacy policy before they can access any Reward SDK features.

Follow the guide below on how to request user consent.

## Usage
[Basic Guide](./doc/basic/README.md)  
[Core API](./doc/core/README.md)  
[API Data](./doc/apiData/README.md)  
[User Consent](./doc/consent/README.md)  
[Migration Guide](./doc/migration/README.md)  
[Event Analytics](./doc/EventAnalytics/README.md)  
[For Java Developers](./doc/java/README.md)  
[KDoc](https://rakuten-ads.github.io/products/mission/android/kdoc/5.1.0/index.html)  
[FAQ](./doc/faq/README.md)

## Version History
[Version History](./doc/history/README.md)

---
LANGUAGE :
> [![jp](./doc/lang/ja.png)](./doc/ja/README.md)
