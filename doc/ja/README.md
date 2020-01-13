<div id="top"></div>

[![Platform](http://img.shields.io/badge/platform-Android-brightgreen.svg?style=flat)](https://developer.android.com)
[![Language](http://img.shields.io/badge/language-Kotlin-green.svg?style=flat)](https://github.com/JetBrains/kotlin)
[![Android](http://img.shields.io/badge/support-API_Level_16+-blue.svg?style=flat)](https://developer.android.com)

# Rakuten Reward SDK ネイティブ

---
# はじめに

<div id="prerequisites"></div>

## 前提

* Android Studio 1.0 以上
* Android API level 16 以上
* Android X をサポート
* Rakuten ID SDKの使用が必須

| バージョン        | OS           | コンパイル OS
--- | --- | ---
|0.1.2|16(4.1)|28 (9.0)|

* アプリ開発者は Android 4.x でのSDKの実装は可能です。ただし、SDK の昨日はAndroid 5以上でサポートしています

<div id="import_sdk"></div>

## Import the Reward SDK
Gradleの依存設定でアプリにインポートすることが出来ます。プロジェクト直下のbuild.gradleのrepositoriesに以下のように参照先を追加する必要があります。

**プロジェクト全体のbuild.gradle サンプル**

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

次に、アプリ直下のbuild.gradleのdependenciesに以下の指定を追加します。

```groovy
  implementation 'com.rakuten.android.ads:rewardsdknative:0.1.1'
```

## 使用方法の説明
[基本ガイド](./basic/README.md)  
[応用ガイド](./advanced/README.md)

## Proguard の設定
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

---
言語 :
> [![jp](../lang/en.png)](../../README.md)



