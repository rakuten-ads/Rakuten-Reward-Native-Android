<div id="top"></div>

[![Platform](http://img.shields.io/badge/platform-Android-brightgreen.svg?style=flat)](https://developer.android.com)
[![Language](http://img.shields.io/badge/language-Kotlin-green.svg?style=flat)](https://github.com/JetBrains/kotlin)
[![Android](http://img.shields.io/badge/support-API_Level_21+-blue.svg?style=flat)](https://developer.android.com)

# Rakuten Reward SDK ネイティブ

---
# はじめに

<div id="prerequisites"></div>

## 前提

* Android Studio 1.0 以上
* Android API level 21 以上
* Android X をサポート
* 楽天 IDSDK もしくは SDKが用意するログインを使用する

| バージョン        | OS           | コンパイル OS
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
|2.3.0|API16 (4.1)|API 29|
|2.3.1|API16 (4.1)|API 29|
|2.3.2|API16 (4.1)|API 29|
|2.3.3|API16 (4.1)|API 29|
|2.4.0|API16 (4.1)|API 30|
|2.4.1|API16 (4.1)|API 30|
|1.1.4|API16 (4.1)|API 30|
|3.0.0|API21 (5.0)|API 30|
|3.1.0|API21 (5.0)|API 30|
|3.1.1|API21 (5.0)|API 30|
|3.1.2|API21 (5.0)|API 30|
|3.2.0|API21 (5.0)|API 30|
|3.2.1|API21 (5.0)|API 30|
|3.3.0|API21 (5.0)|API 30|
|3.4.0|API21 (5.0)|API 31|
|3.4.1|API21 (5.0)|API 33|
|3.4.2|API21 (5.0)|API 33|
|3.5.0|API21 (5.0)|API 33|
|3.5.1|API21 (5.0)|API 33|
|3.6.0|API21 (5.0)|API 33|
|3.7.0|API21 (5.0)|API 33|

<div id="import_sdk"></div>

## リワードSDKをインポートする
Gradleの依存設定でアプリにインポートすることが出来ます。プロジェクト直下のbuild.gradleのrepositoriesに以下のように参照先を追加する必要があります。

**プロジェクト全体のbuild.gradle サンプル**

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

次に、アプリ直下のbuild.gradleのdependenciesに以下の指定を追加します。

```groovy
  implementation 'com.rakuten.android:rewardsdknative-ui:3.7.0'
```

こちらで用意するUIを利用されてない場合は "rewardsdknative-ui"　を入れないことも可能です
```groovy
  implementation 'com.rakuten.android:rewardsdknative-core:3.7.0'
```

※ rewardsdknative-ui モジュールは viewbinding と databinding　を使用いたします。  
もしこちらのモジュールの場合で上記のご利用がない場合, 下記のような記述を build.gradle　に加えてください
```groovy
buildFeatures {
        viewBinding true
        dataBinding true
}
```

バージョン2.0以下をご利用の場合以下のようになります。
```groovy
  implementation 'com.rakuten.android.ads:rewardsdknative:1.1.4'
```

### Android Gradle Plugin 7.0
バージョン 3.６.０ 以降、Reward SDKのAndroid Gradle Plugin (AGP)はバージョン７.１にアップグレードしました。  
アプリのAGPをバージョン７.０以降にアップグレードしてください。
```groovy
dependencies {
    classpath "com.android.tools.build:gradle:7.0.3"
}
```

## 使用方法の説明
[基本ガイド](./basic/README.md)  
[APIガイド](./APIReference/README.md)  
[移行ガイド](./migration/README.md)  
[イベントアナリティクス](./EventAnalytics/README.md)  
[Java](./java/README.md)  
[KDoc](https://rakuten-ads.github.io/products/mission/android/kdoc/3.7.0/index.html)

## 更新履歴
[更新履歴](./history/README.md)

---
言語 :
> [![en](../lang/en.png)](../../README.md)



