[トップ](/README.md#top)　>　[コア API](./README.md)　>  RakutenReward  

コンテンツ  
* [プロパティ](#プロパティ)  
* [公開メソッド](#公開メソッド)  
  * [RakutenRewardListener](#rakutenrewardlistener)  
  * [ミッションリスト](#ミッションリスト)  
  * [ポイント履歴](#ポイント履歴)  
  * [未獲得ミッションリスト](#未獲得ミッションリスト)  
  * [Init API](#init-api)  
  * [アクションを送信する](#アクションを送信する)  
  * [会員情報](#会員情報)  
  * [楽天リワードのページを開く](#楽天リワードのページを開く)  
  * [クッキーをセットする](#クッキーをセットする)  
  * [利用規約への同意をリクエスト](#利用規約への同意をリクエスト)  
  * [通知バナーを表示する](#通知バナーを表示する)  
  * [SDK セッションを開始](#SDK-セッションを開始)  

---  
# RakutenReward
`RakutenReward` クラスはリワードSDKのメインの設定や機能を提供しています。    

## プロパティ  
| プロパティ名                                                | 説明                           |
|-------------------------------------------------------|------------------------------|
| appCode                                               | アプリケーションキー                   |
| [lastFailed](../apiData/README.md#last-failed-method) | 最後にエラーの発生したダイナミックAPIの情報を取得する |
| status                                                | リワードSDKの状態                   |
| tokenType                                             | ログインオプションを切り替える              |
| user                                                  | ユーザーデータ                      |
| version                                               | リワードSDKのバージョン                |  

<details>
    <summary>JAVA</summary>

JAVAで `get` メソッドを使ってプロパティ値をを取得する。  

例  
```java 
RakutenReward.INSTANCE.getAppCode();
```  

</details>  

<br>

## 公開メソッド  
| メソッド名                                                 | 説明                         |
|-------------------------------------------------------|----------------------------|
| [addRakutenRewardListener](#rakutenrewardlistener)    | RakutenRewardListenerを加える  |
| clearAccessToken                                      | トークンを取り除く                  |
| forceClaimClose                                       | ポイントクレイムUI強制的に閉じる          |
| [getMissions](#ミッションリスト)                              | ミッションリストを取得する              |
| [getPointHistory](#ポイント履歴)                            | 3ヶ月前までのポイント履歴を取得する         |
| [getUnclaimedItems](#未獲得ミッションリスト)                     | 未獲得ミッションリストを取得する           |
| [init](#init-api)                                     | リワードSDKの初期化                |
| [logAction](#アクションを送信する)                              | ミッションを達成するためにアクションを送信する    |
| [memberInfo](#会員情報)                                   | 最新の会員情報を取得する               |
| [openHelpPage](#楽天リワードのページを開く)                        | ヘルプページをSDKのミニブラウザーで開く      |
| [openPrivacyPage](#楽天リワードのページを開く)                     | プライバシーポリシーをSDKのミニブラウザーで開く  |
| [openTCPage](#楽天リワードのページを開く)                          | 利用規約をSDKのミニブラウザーで開く        |
| [removeRakutenRewardListener](#rakutenrewardlistener) | RakutenRewardListenerを取り除く |
| [requestForConsent](#利用規約への同意をリクエスト)                  | 利用規約への同意をリクエスト             |
| [setRa](#クッキーをセットする)                                  | Ra クッキーをセットする              |
| setRaeToken                                           | RAE トークンをセットする             |
| setRidToken                                           | RID トークンをセットする             |
| [setRp](#クッキーをセットする)                                  | Rp クッキーをセットする              |
| [setRz](#クッキーをセットする)                                  | Rz クッキーをセットする              |
| [startSession](#SDK-セッションを開始)                         | SDK セッションを開始               |  
| [showConsentBanner](#通知バナーを表示する) | 通知バナーを表示する |

### RakutenRewardListener
RakutenRewardListener 楽天リワードのイベントに関するリスナーです  

| 名前                                                                                                     | 説明               |
|--------------------------------------------------------------------------------------------------------|------------------|
| fun onUnclaimedAchievement(achievement : MissionAchievementData)                                       | ユーザーがミッションを達成した　 |
| fun onUserUpdated(user : RakutenRewardUser)                                                            | ユーザーデータが更新された    |
| fun onSDKStatusChanged(status : RakutenRewardSDKStatus)                                                | SDKの状態が変更された     |
| fun onSDKClaimClosed(missionAchievementData: MissionAchievementData, status: RakutenRewardClaimStatus) | クレイムUIが閉じた       |
| fun onSDKConsentClosed()                                                                               | 同意ダイアログを閉めした     | 
<br>

**RakutenRewardListenerを加える**  
[![support version](http://img.shields.io/badge/core-2.4.1+-green.svg?style=flat)](/doc/history/README.md#version-310)  

```kotlin
RakutenReward.addRakutenRewardListener(this)
```  

> ActivityかFragmentクラスでこのメソッドを使用する場合、Activityが破壊される時メモリリークを防ぐに取り除くAPIを使用してください。  

**RakutenRewardListenerを取り除く**   
[![support version](http://img.shields.io/badge/core-2.4.1+-green.svg?style=flat)](/doc/history/README.md#version-310)  

```kotlin
RakutenReward.removeRakutenRewardListener(this)
```  

詳細については[ここ](/doc/faq/README.md#how-do-i-implement-onsdkstatuschanged-or-onunclaimedachievement)に参考してください。  

<br>  

### ミッションリスト  
こちらの API は [`MissionData`](../apiData/README.md#missiondata) オブジェクトのリストを戻る。  

Kotlin  
```kotlin
RakutenReward.getMissions({ missions ->
    // 成功
}) {
    // 失敗
}
```  

JAVA
```java
RakutenReward.getMissionsJava(new GetMissionsCallback() {
    @Override
    public void success(@NonNull List<MissionData> list) {

    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```  

コルーチン  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
```kotlin
val result : RewardApiResult<List<MissionData>> = RakutenRewardCoroutine.getMissions()
```  

<br>

### ポイント履歴  
こちらの API は [`RakutenRewardPointHistory`](../apiData/README.md#rakutenrewardpointhistory) オブジェクトを戻る。  

Kotlin  
```kotlin
RakutenReward.getPointHistory({ pointHistory ->
    // 成功
}, {
    // 失敗
})
```  

JAVA
```java
RakutenReward.getPointHistoryJava(new PointHistoryCallback() {
    @Override
    public void success(@NonNull RakutenRewardPointHistory rakutenRewardPointHistory) {

    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```  

コルーチン  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
```kotlin
val result : RewardApiResult<RakutenRewardPointHistory> = RakutenRewardCoroutine.getPointHistory()
```   

<br>  

### 未獲得ミッションリスト  
こちらの API は [`MissionAchievementData`](../apiData/README.md#missionachievementdata) オブジェクトのリストを戻る。  

Kotlin  
```kotlin
RakutenReward.getUnclaimedItems({ unclaimed ->
    // 成功
}) {
    // 失敗
}
```  

JAVA
```java
RakutenReward.getUnclaimedItemsJava(new UnclaimedItemCallback() {
    @Override
    public void success(@NonNull List<MissionAchievementData> list) {
        
    }

    @Override
    public void failed(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```  

コルーチン  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
```kotlin
val result : RewardApiResult<List<MissionAchievementData>> = RakutenRewardCoroutine.getUnclaimedItems()
```   

<br>  

### Init API  
リワードSDKの初期化  

> バージョン **3.3.0** から、手動初期化は必要ないようになりました。詳細については[here](../basic/README.md#from-version-330-onward-manual-initialization-is-no-longer-needed)に参考してください。  

```kotlin
RakutenReward.init("<appCode>")
```  

| パラメータ名  | 説明 |
|---------|-----------------------------------------|
| AppCode | アプリケーションキー (こちらは楽天リワードの開発者ポータルから取得できます) | 

**RID, RAEログインオプションの場合**  
  
```kotlin
RakutenReward.init("<appCode>", "<token>")
```  

<br>  

### アクションを送信する  
こちらの API はアクションを送信する。  

Kotlin
```kotlin
RakutenReward.logAction("actionCode", {
    // 送信成功
}) {
    // 送信失敗
}
```  

JAVA  
```java
RakutenReward.logActionJava("actionCode", new LogActionCallback() {
    @Override
    public void success() {
        
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```  

コルーチン  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
```kotlin
val result : RewardApiResult<Unit> = RakutenRewardCoroutine.logAction("actionCode")
```   

<br>  

#### ミッション達成が上限に達した  

[![support version](http://img.shields.io/badge/core-5.2.0+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20240101_v5.2.0)    
ミッション達成がもう上限に達したの場合、`logAction` APIが `MISSION_REACHED_CAP` のエラーコードを戻す。  

<br>  

### 会員情報  
こちらの API は [`RakutenRewardUser`](../apiData/README.md#rakutenrewarduser) オブジェクトを戻る。  

Kotlin  
```kotlin
RakutenReward.memberInfo({ user ->
    // 成功
}) {
    // 失敗
}
```  

JAVA  
```java
RakutenReward.memberInfoJava(new MemberInfoCallback() {
    @Override
    public void success(@NonNull RakutenRewardUser rakutenRewardUser) {
        
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```  

コルーチン  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
```kotlin
val result : RewardApiResult<RakutenRewardUser> = RakutenRewardCoroutine.memberInfo()
```   

<br>  

### 楽天リワードのページを開く  
SDK は各種SDKのページを開くためのAPIを提供しております  

ヘルプページ
```kotlin
RakutenReward.openHelpPage()
```
利用規約  
```kotlin
RakutenReward.openTCPage()
```
プライバシーポリシー
```kotlin
RakutenReward.openPrivacyPage()
```  

<br>  

### クッキーをセットする  
この機能は楽天のアプリケーションですでに広告のためのクッキーを取得している場合に推奨される機能となります。  
もし、デフォルトのログインオプション(`RAKUTEN_AUTH`)をご使用の場合にはこちらの処理はSDKで行いますので、実装する必要はありません。  

**Rzクッキーをセットする**  
```kotlin
RakutenReward.setRz("cookie")
```  

**Rpクッキーをセットする**  
```kotlin
RakutenReward.setRp("cookie")
```

**Raクッキーをセットする**  
[![support version](http://img.shields.io/badge/core-4.1.0+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20230912_v4.1.0)  
```kotlin
RakutenReward.setRa("cookie")
```

<br>  

### 利用規約への同意をリクエスト  
[![support version](http://img.shields.io/badge/core-4.0.0+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20230728_v4.0.0)   

ユーザーがまだ、利用規約に同意していない場合に、同意ダイアログを表示します。  
ユーザーがすでに利用規約を同意していた場合、ダイアログを表示せずに`CONSENT_PROVIDED`ステータスがコールバックに返します。詳細については[ここ](../consent/README.md#利用規約への同意をリクエストする-api)に参考してください。      

このコールバックは[`RakutenRewardConsentStatus`](../apiData/README.md#rakutenrewardconsentstatus)を戻る。    

Kotlin  
```kotlin
RakutenReward.requestForConsent { status ->
    // check consent status
}
```  

JAVA  
```java
RakutenReward.requestForConsentJava(rakutenRewardConsentStatus -> {
    // check consent status
});
```  

### 通知バナーを表示する  
[![support version](http://img.shields.io/badge/core-5.3.0+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20240321_v5.3.0)  

ユーザーがまだ、利用規約に同意していない場合に、通知バナーを表示します。ユーザーが上のバナーをタップして、同意ダイアログを表示される。    
ユーザーがすでに利用規約を同意していた場合、バナーを表示せずに`CONSENT_PROVIDED`ステータスがコールバックに返します。詳細については[ここ](../consent/README.md#通知バナーを表示する)に参考してください。      

このコールバックは[`RakutenRewardConsentStatus`](../apiData/README.md#rakutenrewardconsentstatus)を戻る。    
 

Kotlin 
```kotlin
RakutenReward.showConsentBanner {
    // check consent status
}
```  

JAVA
```java
RakutenReward.showConsentBannerJava(rakutenRewardConsentStatus -> {
    // check consent status
});
```

### SDK セッションを開始  
[![support version](http://img.shields.io/badge/core-3.4.2+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20221202_v3_4_2)  
SDK セッションを手動で開始する。ONLINEになった場合、`RakutenRewardListener#onSDKConsentClosed()` の実装を呼び出します。   

```kotlin
RakutenReward.startSession()
```

---  
言語 :
> [![en](../../lang/en.png)](../../core/RakutenReward.md)  
