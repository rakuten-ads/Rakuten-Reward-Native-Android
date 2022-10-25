[トップ](../README.md#top)　>　イベントアナリティクス

コンテンツ
* [イベントアナリティクスの概要](#イベントアナリティクスの概要)
* [イベントアナリティクスモジュールの導入](#イベントアナリティクスモジュールの導入)
* [イベントアナリティクス機能をオンにする](#イベントアナリティクス機能をオンにする)
* [イベントアナリティクスのイベントをミッションイベントとしても送信する](#convert-analytics-sdk-event-to-mission-event)

---
# イベントアナリティクスの概要
ミッションSDKは新たな機能として"Event Analytics"を導入いたしました。<br>
この機能のメインはアプリケーションのイベントの分析機能を強化したものです。<br>
加えて、通常のアプリケーションのイベントをミッションイベントに変換する機能を通じてミッションSDKをより効果的に利用するための機能が含まれております。<br>


* イベントアナリティクス機能のダッシュボードを開発者ポータルで提供
* 通常のイベントをミッションイベントに変換する機能を提供

# イベントアナリティクスモジュールの導入
こちらの機能を使用するには以下のモジュールを追加します
```groovy
implementation 'com.rakuten.android:rewardsdknative-event:1.0.1'
```
合わせて、Rakuten Analytics SDK 導入する必要があります詳しくはこちら<br>
[Rakuten Analytics SDK for Android](https://github.com/rakutentech/android-analytics) をご参照ください。<br>

# イベントアナリティクス機能をオンにする
イベントアナリティクス機能を有効にセットする

```kotlin
RakutenRewardConfig.setMissionEventFeatureEnabled(true)
```

# イベントアナリティクスのイベントをミッションイベントとしても送信する
こちらは新しい機能になります。<br>
開発者ポータルにて、イベントアナリティクスのイベントとミッションイベントに結びつける設定を行います。<br>

## 使い方
* はじめに、アナリティクスイベント(アクション分析用のイベント)を Mission SDKの
 API を経由して呼び出します。
* もし、アクション分析用のイベントをミッションイベントに紐付ける場合、開発者ポータルの設定でマッピングを作成します
* 紐付け後、 イベントは Analytics SDKと Mission SDKと両方のイベントが送信されます

イベントの送信
```kotlin
RakutenMissionEvent.logAction("actionname", mapOf(), {
   // Success
}, {
   // Failed
})
```

もし、イベントアナリティクスのイベントにメタデータを付与する場合
```kotlin
var map = mutableMapOf<String, Object>()
map["key"] = "value" as Object
RakutenMissionEvent.logAction("actionname", map, {}, {})
```

※ ここでいう actionname は Analytics SDKのアクション名になります,ミッションSDKでのアクションコードではありません

この API は以下のように動作します
* もし、マッピングデータがない場合はAnalytics SDKのアクションのみ送信されます
* もし、マッピングデータがある場合はダッシュボードで定義されたミッションSDKのアクションも送信されます

---
LANGUAGE :
> [![ja](../../lang/en.png)](../../EventAnalytics/README.md)