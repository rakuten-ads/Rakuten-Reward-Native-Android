<div id="top"></div>

[![Platform](http://img.shields.io/badge/platform-Android-brightgreen.svg?style=flat)](https://developer.android.com)
[![Language](http://img.shields.io/badge/language-Kotlin-green.svg?style=flat)](https://github.com/JetBrains/kotlin)
[![Android](http://img.shields.io/badge/support-API_Level_24+-blue.svg?style=flat)](https://developer.android.com)

# Rakuten Reward SDK ネイティブ

---
# はじめに

<div id="prerequisites"></div>

## 前提

* Android Studio Arctic Fox 以上
* Android API level 24 以上
* Android X をサポート
* 楽天 IDSDK もしくは SDKが用意するログインを使用する

| バージョン | 最小限 OS      | コンパイル OS |
|-------|-------------|----------|
| 7.3.0 | API24 (7.0) | API 35   |
| 7.2.1 | API24 (7.0) | API 35   |
| 7.2.0 | API24 (7.0) | API 35   |
| 7.1.1 | API24 (7.0) | API 35   |
| 7.1.0 | API24 (7.0) | API 35   |
| 7.0.1 | API24 (7.0) | API 35   |
| 7.0.0 | API24 (7.0) | API 35   |
| 6.2.0 | API24 (7.0) | API 34   |
| 6.1.0 | API24 (7.0) | API 34   |
| 6.0.1 | API24 (7.0) | API 34   |
| 6.0.0 | API24 (7.0) | API 34   |

<details>
    <summary>古いバージョン</summary>

| バージョン | 最小限 OS      | コンパイル OS |
|-------|-------------|----------|
| 5.4.1 | API24 (7.0) | API 34   |
| 5.4.0 | API24 (7.0) | API 34   |
| 5.3.0 | API24 (7.0) | API 34   |
| 5.2.1 | API24 (7.0) | API 34   |
| 5.2.0 | API24 (7.0) | API 34   |
| 5.1.0 | API24 (7.0) | API 34   |
| 5.0.0 | API24 (7.0) | API 34   |
| 4.1.0 | API24 (7.0) | API 33   |
| 4.0.0 | API21 (5.0) | API 33   |
| 3.7.0 | API21 (5.0) | API 33   |
| 3.6.0 | API21 (5.0) | API 33   |
| 3.5.1 | API21 (5.0) | API 33   |
| 3.5.0 | API21 (5.0) | API 33   |
| 3.4.2 | API21 (5.0) | API 33   |
| 3.4.1 | API21 (5.0) | API 33   |
| 3.4.0 | API21 (5.0) | API 31   |
| 3.3.0 | API21 (5.0) | API 30   |
| 3.2.2 | API21 (5.0) | API 30   |
| 3.2.1 | API21 (5.0) | API 30   |
| 3.2.0 | API21 (5.0) | API 30   |
| 3.1.2 | API21 (5.0) | API 30   |
| 3.1.1 | API21 (5.0) | API 30   |
| 3.1.0 | API21 (5.0) | API 30   |
| 3.0.0 | API21 (5.0) | API 30   |
| 1.1.4 | API16 (4.1) | API 30   |
| 2.4.1 | API16 (4.1) | API 30   |
| 2.4.0 | API16 (4.1) | API 30   |
| 2.3.3 | API16 (4.1) | API 29   |
| 2.3.2 | API16 (4.1) | API 29   |
| 2.3.1 | API16 (4.1) | API 29   |
| 2.3.0 | API16 (4.1) | API 29   |
| 2.2.2 | API16 (4.1) | API 29   |
| 2.2.1 | API16 (4.1) | API 29   |
| 2.2.0 | API16 (4.1) | API 29   |
| 2.1.0 | API16 (4.1) | API 29   |
| 2.0.0 | API16 (4.1) | API 29   |
| 1.1.3 | API16 (4.1) | API 29   |
| 1.1.2 | API16 (4.1) | API 29   |
| 1.1.1 | API16 (4.1) | API 29   |
| 1.1.0 | API16 (4.1) | API 29   |
| 1.0.0 | API16 (4.1) | API 29   |

</details>

<div id="import_sdk"></div>

## リワードSDKをインポートする
Gradleの依存設定でアプリにインポートすることが出来ます。プロジェクト直下のbuild.gradleのrepositoriesに以下のように参照先を追加する必要があります。

**プロジェクト全体のbuild.gradle サンプル**

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

次に、アプリ直下のbuild.gradleのdependenciesに以下の指定を追加します。 

### Reward Android BoM（部品構成表）  
Reward Native Android 部品構成表（部品構成表）は、1 つのバージョン（BoM のバージョン）のみを指定することで、すべてのライブラリ バージョンを管理できます。  

アプリで Reward Native BoM を使用する場合、BoM は BoM のバージョンにマッピングされた個々のライブラリ バージョンを自動的に取得します。アプリで BoM のバージョンを更新すると、アプリで使用するすべてのライブラリが、その BoM のバージョンにマッピングされたバージョンに更新されます。  

Reward Native Android 部品構成表を使用して、モジュール（アプリレベル）の Gradle ファイル（通常は app/build.gradle）で依存関係を宣言する方法は次のとおりです。BoM を使用する場合、依存関係の行にライブラリのバージョンを個別に指定しないでください。  
```groovy

dependencies {
  // Import the BoM for the Reward Native platform
  implementation platform('com.rakuten.android:rewardsdknative-bom:7.3.0')

  // Declare the dependency for the core library
  implementation 'com.rakuten.android:rewardsdknative-core' 
  // Declare the dependency for the built-in UI
  implementation 'com.rakuten.android:rewardsdknative-ui'
}
```  
BOMに関する問題は[ここ](../faq/README.md#bom)に参考してくっださい。

<details>
  <summary>Pre-6.0.0</summary>

```groovy
  implementation 'com.rakuten.android:rewardsdknative-ui:5.4.1'
```

こちらで用意するUIを利用されてない場合は "rewardsdknative-ui"　を入れないことも可能です
```groovy
  implementation 'com.rakuten.android:rewardsdknative-core:5.4.1'
```

</details>  
<br>

※ rewardsdknative-ui モジュールは viewbinding と databinding　を使用いたします。  
もしこちらのモジュールの場合で上記のご利用がない場合, 下記のような記述を build.gradle　に加えてください
```groovy
buildFeatures {
        viewBinding true
        dataBinding true
}
```

# Android Gradle Plugin 7.0
バージョン 3.６.０ 以降、Reward SDKのAndroid Gradle Plugin (AGP)はバージョン７.１にアップグレードしました。  
アプリのAGPをバージョン７.０以降にアップグレードしてください。
```groovy
dependencies {
    classpath "com.android.tools.build:gradle:7.0.3"
}
```

# 利用規約への同意をリクエストする
バージョン 4.0.0 以降、Reward SDKの機能を使う前に、ユーザーがRewardの利用規約および個人情報保護方針へのご同意が必須となります。

## 使用方法の説明
[基本ガイド](./basic/README.md)  
[コアAPI](./core/README.md)  
[APIデータ](./apiData/README.md)  
[利用規約への同意について](./consent/README.md)  
[移行ガイド](./migration/README.md)  
[イベントアナリティクス](./EventAnalytics/README.md)  
[JavaScript 拡張機能](./extension/README.md)  
[Java](./java/README.md)  
[KDoc](https://rakuten-ads.github.io/products/mission/android/kdoc/7.3.0/index.html)

## 更新履歴
[更新履歴](./history/README.md)

---
言語 :
> [![en](../lang/en.png)](../../README.md)



