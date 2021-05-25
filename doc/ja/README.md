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
* 楽天 IDSDK もしくは SDKが用意するログインを使用する

| バージョン        | OS           | コンパイル OS
--- | --- | ---
|1.0.0|API16 (4.1)|API 29|
|1.1.0|API16 (4.1)|API 29|
|1.1.1|API16 (4.1)|API 29|
|1.1.2|API16 (4.1)|API 29|
|2.0.0|API16 (4.1)|API 29|
|2.1.0|API16 (4.1)|API 29|
|2.2.0|API16 (4.1)|API 29|


* アプリ開発者は Android 4.x でのSDKの実装は可能です。ただし、SDK の昨日はAndroid 5以上でサポートしています

<div id="import_sdk"></div>

## リワードSDKをインポートする
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
  implementation 'com.rakuten.android:mission-ui:2.2.0'
```

こちらで用意するUIを利用されてない場合は "rewardsdknative-ui"　を入れないことも可能です
```groovy
  implementation 'com.rakuten.android:rewardsdknative-core:2.2.0'
```

バージョン2.0以下をご利用の場合以下のようになります。
```groovy
  implementation 'com.rakuten.android.ads:rewardsdknative:1.1.2'
```


## 使用方法の説明
[基本ガイド](./basic/README.md)  
[APIガイド](./APIReference/README.md)

## 更新履歴
[更新履歴](./history/README.md)

---
言語 :
> [![en](../lang/en.png)](../../README.md)



