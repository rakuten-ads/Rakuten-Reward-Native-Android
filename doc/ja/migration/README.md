[トップ](../README.md#top)　> 移行ガイド

コンテンツ
* [バージョン 3.3.0 に移行する](#バージョン-330-に移行する)
    * [SDKの初期化](#sdkの初期化)
    * [廃止予定のメソッド](#廃止予定のメソッド)
* [バージョン 3.1.0 に移行する](#バージョン-310-に移行する)
---
# バージョン 3.3.0 に移行する
### SDKの初期化
* アプリケーションのAndroidManifest.xmlに`App Code`を設定してくだたさい。
```xml
<application>
    <!-- Reward SDK Application Key -->
    <meta-data
        android:name="com.rakuten.gap.ads.mission_core.appKey"
        android:value="{Application Key}"/>
</application>
```
* この`init`メソッドをコードから取り除いてください
```kotlin
RakutenReward.init(context, "<AppCode>")
```

#### RAE, RID ログインオプションを使っている方
* この`init`メソッドを使っているなら、取り除いてください
```kotlin
RakutenReward.init("<AppCode>", "<Token>")
```
* このAPIでトークンを設定する
```kotlin
// for RID login option
RakutenReward.setRIdToken("token")

// for RAE login option
RakutenReward.setRaeToken("token")
```
<br/>

### 廃止予定のメソッド
この以下 `Context` が必要なメソッドは廃止予定になりました。新しい API は `Context` が必要ないです。
* `RakutenAuth.getUserName(context)`
* `RakutenRewardConfig.setOptedOut(context, optedOut)`
* `RakutenRewardConfig.setUiEnabled(context, uiEnabled)`

<br/><br/>

# バージョン 3.1.0 に移行する
`RakutenReward.listener`のヴァリアブルは廃止予定になりました。この以下のAPIを使ってリスナーのインスタンスを提供してください。

**NOTE: Activityクラスを`RakutenRewardBaseActivity`クラスから拡張する場合、`RakutenRewardListener`のインスタンスを提供するのは必要ないです。Activityクラスでリスナーのメソッドをオーバーライドができます。**

* `RakutenRewardListener`のインスタンスを提供する場合
```kotlin
override fun onResume() {
    super.onResume()
    RakutenReward.addRakutenRewardListener(listener)
}
```

* メモリリークを回避するためこのAPIを使ってリスナーのインスタンスを取り除く
```kotlin
override fun onPause() {
    super.onPause()
    RakutenReward.removeRakutenRewardListener(listener)
}
```

---
言語 :
> [![en](../../lang/en.png)](../../migration/README.md)