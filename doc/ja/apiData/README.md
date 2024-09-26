[トップ](../README.md#top)　> APIデータ  

コンテンツ  
* [MissionAchievementData](#missionachievementdata)  
* [MissionData](#missiondata)  
* [MissionLiteData](#missionlitedata)
* [RakutenRewardPointHistory](#rakutenrewardpointhistory)  
* [RakutenRewardPoint](#rakutenrewardpoint)  
* [RakutenRewardUser](#rakutenrewarduser)  
* [Status](#status)  
  * [RakutenRewardSDKStatus](#rakutenrewardsdkstatus)  
  * [RakutenRewardClaimStatus](#rakutenrewardclaimstatus)  
  * [RakutenRewardConsentStatus](#rakutenrewardconsentstatus)  
  * [RewardApiResult](#rewardapiresult)  
  * [RakutenRewardAPIError](#rakutenrewardapierror)  
  * [Last Failed Method](#last-failed-method)  

---  

# APIデータ  


## MissionAchievementData 
| パラメータ名           | 説明                         |
|------------------|----------------------------|
| name             | ミッション名                     |
| iconurl          | アイコンのURL                   |
| instruction      | ミッションの説明                   |
| action           | アクションコード(キー)               |
| custom           | ミッションのノーティフィケーションがカスタムかどうか |
| notificationtype | ミッションのノーティフィケーションタイプ       |
| point            | ポイント                       |
| unclaimed        | 未獲得ミッション件数                 |
| achievedDate     | ミッション達成日                   | 

---  

## MissionData  

| パラメータ名           | 説明                                                                                | 例                                                                           |
|------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| name             | ミッション名                                                                            | Mission A                                                                   |
| actionCode       | アクションコード                                                                          | ZIJCjBeQBHac8nJa                                                            |
| iconurl          | ミッションアイコンのURL                                                                     | https://mprewardsdk.blob.core.windows.net/sdk-portal/appCode/actionCode.png |
| instruction      | ミッションの説明文                                                                         | 1日1回プレイする                                                                   |
| condition        | ミッションの達成条件                                                                        | 毎日10回達成可能                                                                   |
| notificationtype | ミッションのノーティフィケーションタイプ                                                              | NONE, BANNER, MODAL, CUSTOM, BANNER_50, BANNER_250                          |
| point            | ミッションのポイント                                                                        | 10                                                                          |
| enddatestr       | ミッションの終了日 <br> 日次の場合 : Today<br> 週次 : 週の終わり<br> 月次 : 月の終わり<br> カスタム : 指定された日時<br> | 20190403                                                                    |
| till             | ミッション終了日までの残り日数                                                                   | 残り3日                                                                        |
| ext              | ミッションのための拡張データ                                                                    |                                                                             |
| reachedCap       | ミッション達成が上限に達したかどうか？                                                               | true                                                                        |
| times            | ミッション達成に必要なアクション数                                                                 | 3                                                                           |
| progress         | 現在のアクションの状態                                                                       | 1                                                                           |

---

## MissionLiteData  

| パラメータ名           | 説明                                                                                | 例                                                                           |
|------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| name             | ミッション名                                                                            | Mission A                                                                   |
| actionCode       | アクションコード                                                                          | ZIJCjBeQBHac8nJa                                                            |
| iconurl          | ミッションアイコンのURL                                                                     | https://mprewardsdk.blob.core.windows.net/sdk-portal/appCode/actionCode.png |
| instruction      | ミッションの説明文                                                                         | 1日1回プレイする                                                                   |
| condition        | ミッションの達成条件                                                                        | 毎日10回達成可能                                                                   |
| notificationtype | ミッションのノーティフィケーションタイプ                                                              | NONE, BANNER, MODAL, CUSTOM, BANNER_50, BANNER_250                          |
| point            | ミッションのポイント                                                                        | 10                                                                          |
| enddatestr       | ミッションの終了日 <br> 日次の場合 : Today<br> 週次 : 週の終わり<br> 月次 : 月の終わり<br> カスタム : 指定された日時<br> | 20190403                                                                    |
| till             | ミッション終了日までの残り日数                                                                   | 残り3日                                                                        |
| ext              | ミッションのための拡張データ                                                                    |                                                                             |
| times            | ミッション達成に必要なアクション数                                                                 | 3                                                                           |

---

## RakutenRewardPointHistory  
`RakutenRewardPoint` インスタンスのリストになります  

## RakutenRewardPoint  

| パラメータ名    | 説明             |
|-----------|----------------|
| point     | ポイント数          |
| pointdate | ポイント付与月 YYYYMM |  

---  

## RakutenRewardUser  
`RakutenRewardUser` ユーザデータのクラスです

| パラメータ名          | 説明                   |
|-----------------|----------------------|
| unclaimed       | 未獲得ミッションの数           |
| signin          | 　ユーザーがサインインしているかどうか？ |
| point           | リワードサービスで取得したポイント    |
| achievementList | ミッションリスト(使用していない)    |

---  

## Status  

### RakutenRewardSDKStatus  
RakutenRewardSDKStatus は Reward SDK の状態を管理するクラスです

| 名前               | 説明　                                              |
|------------------|--------------------------------------------------|
| ONLINE           | SDKの初期化が完了 SDKのメンバー情報が正しく更新された(ポイントおよび未獲得ミッション数) |
| OFFLINE          | SDKの初期化が未完了または失敗                                 |
| APPCODEINVALID   | アプリケーションキーが間違っている                                |
| TOKENEXPIRED     | トークンの期限切れ                                        |
| USER_NOT_CONSENT | ユーザーまだ利用規約に同意しない                                 |
---  

<br>

### RakutenRewardClaimStatus

| Enum    | 説明          |
|---------|-------------|
| NOTYET  | まだクレイムしていない |
| SUCCESS | クレイム成功      |
| FAIL    | クレイム失敗      |  
---  

<br>

### RakutenRewardConsentStatus

| RakutenRewardConsentStatus              | 説明                         |
|-----------------------------------------|----------------------------|
| CONSENT_PROVIDED                        | 同意しました                     |
| CONSENT_NOT_PROVIDED                    | 同意していません                   |
| CONSENT_FAILED                          | APIエラーが発生しました              |
| CONSENT_PROVIDED_RESTART_SESSION_FAILED | 同意しましたが、SDKセッションの再開に失敗しました | 
---  

<br>

### RewardApiResult
`RakutenRewardCoroutine`の戻る値  

#### Success  
| パラメータ名 | 説明              |
|--------|-----------------|
| data   | API data object |

#### Failed  
| パラメータ名 | 説明                      |
|--------|-------------------------|
| error  | `RakutenRewardAPIError` |  

---  

<br>  

### RakutenRewardAPIError  

| Enum                | 説明                                              |
|---------------------|-------------------------------------------------|
| NETWORKERROR        | ネットワークエラー(接続失敗)                                 |
| APIRESPONSEERROR    | ネットワークのレスポンスに問題があった(基本的には起こりません)                |
| TOKENEMPTY          | 	アクセストークンがセットされていない                             |
| SDKNOTACTIVE        | SDKが初期化されていません                                  |
| TOKENEXPIRE         | アクセストークンの有効期限がきれています <br> アクセストークンをリフレッシュしてください |
| UNKNOWN             | 不明なエラー(基本的には起こりません)                             | 
| USER_NOT_CONSENT    | ユーザーまだ利用規約に同意しない                                | 
| MISSION_REACHED_CAP | ミッション達成がもう上限に達した                                |  
---  

<br>

### Last Failed Method  
SDKはアプリケーションでエラーを処理できるようにAPIが失敗した場合にその詳細を提供します    

#### RakutenRewardAPILastCalled  
| Property Name | Description                                    |
|---------------|------------------------------------------------|
| method        | The last failed API in `RakutenRewardAPI` enum |
| parameters    | Parameters for the API call                    |  

#### RakutenRewardAPI enum  

| 名前              | 説明(関数名)                        |
|-----------------|--------------------------------|
| MEMBERINFO      | memberInfo                     |
| LOGACTION       | logAction                      |
| GETUNCLAIM      | getUnclaimedItems              |
| POINTHISTORY    | getPointHistory                |
| CLAIM           | claim (MissionAchievementData) |
| GETMISSIONLIST  | getMissions                    |  
| PROVIDE_CONSENT | provideConsent                 |


---  
言語 :
> [![en](../../lang/en.png)](../../apiData/README.md)  
