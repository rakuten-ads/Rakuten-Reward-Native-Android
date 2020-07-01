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
|0.2.0|16(4.1)|28 (9.0)|
|1.0.0|16(4.1)|28 (9.0)|
|1.1.0|16(4.1)|28 (9.0)|


* アプリ開発者は Android 4.x でのSDKの実装は可能です。ただし、SDK の昨日はAndroid 5以上でサポートしています

<div id="import_sdk"></div>

## Import the Reward SDK
Gradleの依存設定でアプリにインポートすることが出来ます。プロジェクト直下のbuild.gradleのrepositoriesに以下のように参照先を追加する必要があります。

**プロジェクト全体のbuild.gradle サンプル**

```groovy

allprojects {
    repositories {
        jcenter()
        maven { url 'https://raw.github.com/rakuten-ads/rakuten-ads-android/master/maven' }
        maven { url 'https://raw.github.com/rakuten-ads/rakuten-reward-native-android/master/maven' }
    }
}
```

次に、アプリ直下のbuild.gradleのdependenciesに以下の指定を追加します。

```groovy
  implementation 'com.rakuten.android:rewardsdknative:1.1.0'
```

## 使用方法の説明
[基本ガイド](./basic/README.md)  
[応用ガイド](./advanced/README.md)

---
言語 :
> [![en](../lang/en.png)](../../README.md)



