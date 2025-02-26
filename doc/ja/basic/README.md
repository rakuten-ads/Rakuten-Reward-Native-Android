[トップ](../README.md#top)　>基本ガイド

コンテンツ
* [認証](#認証)<br>
  * [ログインオプション](#ログインオプション)<br>
  * [ログイン](#ログイン)<br>
  * [ログアウト](#ログアウト)<br>
* [SDKの初期化](#sdkの初期化)<br>
* [SDKステータス](#sdkステータス)<br>
* [ユーザー情報を取得する](#ユーザー情報を取得する)<br>
* [ミッションの達成](#ミッションの達成)<br>
* [SDK用意するUI](#sdk用意するui)<br>
* [SDKデバッグログ](#SDKデバッグログ)<br>
* [コルーチン サポート](#コルーチン-サポート)<br><br>

---

# 認証

## ログインオプション
リワードSDK では3種類のログイン方法を提供しております。  
ご利用の環境に合わせて、適切なものをご利用ください。  
初期設定では、RAKUTEN_AUTH　になっております。  

***注意: RAEは2025年までに廃止されます。***

| ログインオプション    | 説明                                                 |
|--------------|----------------------------------------------------|
| RAKUTEN_AUTH | 初期設定、ログインやユーザーの処理を全てリワードSDKが担当します                  |
| RID          | ログイン部分はID SDKが担当します(RID)。トークンをリワードSDKに渡す必要があります    |  
| RAE          | ログイン部分はUser SDKが担当します(RAE)。 トークンをリワードSDKに渡す必要があります |  
<br>

## ログインオプションを切り替える

初期設定では、リワードSDKが用意したログインになります。(RAKUTEN_AUTH)  
<br>

### RAKUTEN_AUTH
```kotlin
RakutenReward.tokenType = RakutenRewardTokentype.RAKUTEN_AUTH
```
<details>
    <summary>JAVA</summary>

```java
RakutenReward.INSTANCE.setTokenType(RakutenRewardTokentype.RAKUTEN_AUTH);
```    
</details>
<br>   

### RID
```kotlin
RakutenReward.tokenType = RakutenRewardTokentype.RID
```
<details>
    <summary>JAVA</summary>

```java
RakutenReward.INSTANCE.setTokenType(RakutenRewardTokentype.RID);
```    
</details>  
リワードSDKのAPIを利用するには、トークンの設定が必要です  
```kotlin
RakutenReward.setRIdToken("token")
```

ログインの実装方法についてはID　SDK の詳細をご参照ください。

> :grey_exclamation:  **バージョン3.1.１から、ユーザーがログアウト時にトークンやデータをちゃんと消すためにログアウトAPIを呼ぶ必要があります。**

[ログアウト](#ログアウト) に参照  
<br>

### RAE  
***このAPIは廃止予定になります***
```kotlin
RakutenReward.tokenType = RakutenRewardTokentype.RAE
```
<details>
    <summary>JAVA</summary>

```java
RakutenReward.INSTANCE.setTokenType(RakutenRewardTokentype.RAE);
```    
</details>  

リワードSDKのAPIを利用するには、トークンの設定が必要です  
```kotlin
RakutenReward.setRaeToken("token")
```

ログインの実装方法についてはUser　SDK の詳細をご参照ください。

> :grey_exclamation:  **バージョン3.1.１から、ユーザーがログアウト時にトークンやデータをちゃんと消すためにログアウトAPIを呼ぶ必要があります。**

[ログアウト](#ログアウト) に参照  
<br>  

# ログイン  
[ここ](./LOGIN.md)に参考してください。  
楽天ログインSDKを使うの場合、これは必要ないです。 

<br>  


# ログアウト
ユーザーをログアウトする。  
> ユーザーがログアウト時にトークンやデータをちゃんと消すためにログアウトAPIを呼ぶ必要があります。  

```kotlin
private fun logout() {
    RakutenAuth.logout(object : LogoutResultCallback {
        override fun logoutSuccess() {
            //ログアウト 完了
        }

        override fun logoutFailed(e: RakutenRewardAPIError) {
            //ログアウト失敗
        }
    })
}
```
<details>
    <summary>JAVA</summary>

```java
RakutenAuth.logout(new LogoutResultCallback() {
    @Override
    public void logoutSuccess() {
        //ログアウト完了
    }

    @Override
    public void logoutFailed(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {
        //ログアウト失敗
    }
});
```    
</details>  

<br><br>


# SDKの初期化
楽天リワードSDKを利用するにははじめに初期化が必要です(SDKユーザーの基本データを取得します)
SDKの機能を利用するのにはRakutenRewardクラスのメソッドを利用します

```kotlin
class App: Application() {

    override fun onCreate() {
        super.onCreate()
        //init sdk with your App Code
        RakutenReward.init("<AppCode>")
    }
}
```

| パラメータ名  | 説明 |
|---------|-----------------------------------------|
| AppCode | アプリケーションキー (こちらは楽天リワードの開発者ポータルから取得できます) |

<br/>

### **\*バージョン 3.3.0 から、手動初期化は必要ないようになりました。**
アプリケーションのAndroidManifest.xmlに`App Code`を設定してくだたさい。
```xml
<application>
    <!-- Reward SDK Application Key -->
    <meta-data
        android:name="com.rakuten.gap.ads.mission_core.appKey"
        android:value="{Application Key}"/>
</application>
```
  
<br>

## 楽天のIDSDKを利用する場合  
楽天のIDSDKを使用し、ログインオプションに 、RID, RAE を選択した場合
アプリケーションキーの他にトークンを渡す必要があります。

<br><br/>

## Activity と紐づけてSDK機能をアクティブにする:

### 1 RakutenRewardLightBaseActivity を拡張した Activity クラスを作る
```kotlin
class YourActivity : RakutenRewardBaseActivity {}
```

### 2 Android のライフサイクル上でメソッドをコールする
```kotlin
class YourActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        RakutenRewardLifecycle.onCreate(this)
    }

    override fun onStart() {
        super.onStart()
        RakutenRewardLifecycle.onStart(this)
    }

    override fun onResume() {
        RakutenRewardLifecycle.onResume(this)
    }

    override fun onDestroy() {
        super.onDestroy()
        RakutenRewardLifecycle.onDestroy()
    }
}
```


### 3 AndroidX ライフサイクルイベントをバインドする
```kotlin
class YourActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        RakutenRewardManager.bindRakutenRewardIn(this, this)
    }

}
```

この方法で行うためには Activity に LifecycleOwner を実装する必要があります

---  
<br>  

# SDKステータス  
APIを使用するには、まずSDKステータスがONLINEに切り替わっていることを確認する必要があります。   
SDKステータスを取得する方法は2つあります: 

## RakutenReward.status  
`RakutenReward.status` に直接アクセスして現在のSDKステータスを取得します。  

## RakutenRewardListener  
[`RakutenRewardListener`](../core/RakutenReward.md#rakutenrewardlistener) を追加して、SDKステータスが変更されたときに通知を受け取ります。  
```kotlin  
RakutenReward.addRakutenRewardListener(object : RakutenRewardListener {
    override fun onSDKStatusChanged(status: RakutenRewardSDKStatus) {
        if (status == RakutenRewardSDKStatus.ONLINE) {
            // SDKステータスがONLINEです
        }
    }
})
```  
***注意: [Option 1](#1-rakutenrewardlightbaseactivity-を拡張した-activity-クラスを作る)を使用している場合、RakutenRewardListenerを追加する必要はありません。メソッドを直接オーバーライドできます。***


# ユーザー情報を取得する  
[ここ](./UserInfo.md)に参考してください。  
> こちらのAPIは `RAKUTEN_AUTH` のみ使える    
---  
<br>

# ミッションの達成
ミッションを達成するには、[ここ](./MissionAchivement.md)に参考してください。   

---  
<br>

# SDK用意するUI  
[ここ](./SdkPortal.md)に参考してください。

---  
<br>


# SDKデバッグログ

バージョン3.1.1以降、SDKデバッグログをできようになります。ApplicationクラスでこのAPIを使ってください。
```kotlin
override fun onCreate() {
    if (BuildConfig.DEBUG) {
        RakutenRewardConfig.isDebuggable()
    }
}
```  
<details>
    <summary>JAVA</summary>

```java
@Override
public void onCreate() {
    if (BuildConfig.DEBUG) {
        RakutenRewardConfig.isDebuggable();
    }
}
```    
</details>  

**DEBUGモードだけにこのAPIを使ってください。**

このAPIを使って、SDKロゴを見られます。タグは `RakutenRewardSDK`。

<br>

# コルーチン サポート

[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
SDK は suspend 関数の API を提供しています。
suspend 関数の API は `RakutenRewardCoroutine`クラスにあります。[ここ](../APIReference/README.md#rakutenrewardcoroutine)に参照してください。

suspend 関数の API を使う場合、コルーチンのスコープで呼んでください。例えば、 `viewModelScope` もしくわ `lifecycleScope`。
```kotlin
lifecycleScope.launch { 
    val result = RakutenRewardCoroutine.getMissions()
    when (result) {
        is Failed -> {
            // 失敗ケース
            result.error // エラーコード
        }
        is Success -> {
            // 成功ケース
            val missionList = result.data
        }
    }
}
```
<br>

---
言語 :
> [![en](../../lang/en.png)](../../basic/README.md)
