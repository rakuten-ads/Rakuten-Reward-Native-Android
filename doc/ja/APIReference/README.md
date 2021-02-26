[TOP](../README.md#top)　> APIガイド

コンテンツ
* [RakutenReward](#rakutenreward)<br>
* [RakutenAuth](#rakutenauth)<br>
* [RakutenRewardConfig](#rakutenrewardconfig)<br>
* [楽天リワードのページを開く](#楽天リワードのページを開く)<br>
* [RakutenRewardUser](#rakutenrewarduser)<br>
* [RakutenAuthUserInfo](#rakutenauthuserinfo)
* [Rank](#rank)
* [RakutenRewardListener](#rakutenrewardlistener)
* [RakutenRewardStatus](#rakutenrewardstatus)<br>
* [RakutenAuth](#rakutenauth)
* [LoginResultCallback](#loginresultcallback)
* [LogoutResultCallback](#logoutresultcallback)
* [API Data](#api-data)<br>
  * [MissionData](#missiondata)<br>
  * [RakutenRewardPointHistory](#rakutenrewardpointhistory)<br>
  * [RakutenRewardPoint](#rakutenrewardpoint)<br>
  * [MissionAchievementData](#missionachievementdata)<br>
* [API Errors](#api-errors)<br>
* [Last Failed Method](#last-failed-method)<br>
* [RakutenRewardClaimStatus](#rakutenrewardclaimstatus)<br>
* [ミッションのリストを取得する](#ミッションのリストを取得する)<br>
* [RakutenRewardAdConfiguration](#rakutenrewardadconfiguration)<br>
* [ミッション達成後のカスタムUIの作り方](#ミッション達成後のカスタムUIの作り方)<br><br>


# APIガイド
## RakutenReward
---
RakutenReward クラスはリワードSDKのメインの設定や機能を提供しています

| API 名 | 説明 | 使用例
| --- | --- | ---
| バージョンの取得 |  リワードSDKのバージョンを取得する | `RakutenReward.version`
| SDK ポータルを開く | SDKポータルを開く | `RakutenReward.openSDKPortal()`
| ヘルプページを開く | ヘルプページをSDKのミニブラウザーで開く | `RakutenReward.openHelpPage()`
| 利用規約を開く | 利用規約をSDKのミニブラウザーで開く | `RakutenReward.openTCPage()`
| プライバシーポリシーを開く | プライバシーポリシーをDKのミニブラウザーで開く | `RakutenReward.openPrivacyPage()`
| ミッションリストを取得する | ミッションリストを取得する | `RakutenReward.getMissions( { missions -> <br> // Get Missions <br> }, { // Failed<br> })`
| ポイント履歴を取得する | 3ヶ月前までのポイント履歴を取得する | `RakutenReward.getPointHistory({ pointHistory -> <br> // Get Point History <br> }, { <br> // Failed <br>})`
| アクションを送信する | ミッションを達成するためにアクションを送信する | `RakutenReward.logAction("xxxxxx", { <br> // Success <br>}, { <br> // Failed <br>})`
| 未獲得ミッションを取得する | 未獲得ミッションリストを取得する | `RakutenReward.getUnclaimedItems({ missions -> <br> // Unclaim Mission List <br> }, { <br>// Error <br>})`
| 最後にエラーの発生したダイナミックAPIの情報 | 最後にエラーの発生したダイナミックAPIの情報を取得する | `RakutenReward.lastFailed`

## RakutenAuth
---
| API 名 | 説明 | 使用例 |
| --- | --- | --- |
| ログイン | ログインページを開く | `RakutenAuth.openLoginPage(activity: Activity, requestCode: Int)` |
| ログイン状態の確認 | ログインしているかどうか状態を取得する  | `RakutenAuth.hasUserSignedIn()` |
| ログアウト |  ログアウトする  | `RakutenAuth.logout(object : LogoutResultCallback)` |
| 楽天会員名を取得 | 楽天会員名を取得する | `RakutenAuth.getUserName(context: Context)` |
| 楽天ランクとポイントを取得する | 楽天ランクとポイントを取得する  | `RakutenAuth.RakutenAuth.getUserInfo(success = { userInfo <br>-> <br>}, {<br> // Error <br>})` |


## RakutenRewardConfig
---
RakutenRewardConfig　はユーザー設定を管理するクラスです

| API 名 | 説明 | Example 
| --- | --- | ---
| オプトアウトの取得 | オプトアウトの状態を取得する <br>true : オプトアウト (リワードSDKは動作しません) | RakutenRewardConfig.isOptedOut()
| オプトアウトの設定 | オプトアウトの状態を設定する | RakutenRewardConfig.setOptedOut(context, true)
| UI設定の取得 |  ミッションのUIのオン・オフ設定設定を取得する | RakutenRewardConfig.isUiEnabled()
| UI設定 | ミッションのUIのオン・オフ設定 | RakutenRewardConfig.setUiEnabled(context, true)

## 楽天リワードのページを開く

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

## RakutenRewardUser
---
RakutenRewardUser ユーザデータのクラスです

| パラメータ名 | 説明 |
| --- | ---
| unclaimed | 未獲得ミッションの数
| signin | 　ユーザーがサインインしているかどうか？
| point | リワードサービスで取得したポイント
| achievementList | ミッションリスト(使用していない)  


## RakutenAuthUserInfo
---
楽天会員情報  

| パラメータ名 | 説明 |
| --- | ---
| points | 楽天ポイント合計
| rank | 楽天会員ランク

### 会員ランク
---
日本のみ  

| ランク | 説明
| --- | ---
| 1 | レギュラー会員 |
| 2 | シルバー会員 |
| 3 | ゴールド会員 |
| 4 | プラチナ会員 |
| 5 | ダイヤモンド会員 |

## RakutenRewardListener
---
RakutenRewardListener 楽天リワードのイベントに関するリスナーです

| 名前 | 説明 |
| --- | ---
| fun onUnclaimedAchievement(achievement : MissionAchievementData) | ユーザーがミッションを達成した　
| fun onUserUpdated(user : RakutenRewardUser) | ユーザーデータが更新された
| fun onSDKStatusChanged(status : RakutenRewardSDKStatus) | SDKの状態が変更された
| fun onSDKClaimClosed(missionAchievementData: MissionAchievementData, status: RakutenRewardClaimStatus) | クレイムUIが閉じた

### RakutenRewardSDKStatus
---
RakutenRewardSDKStatus は Reward SDK の状態を管理するクラスです  

| 名前 | 説明　|
| --- | ---
| ONLINE | SDKの初期化が完了 SDKのメンバー情報が正しく更新された(ポイントおよび未獲得ミッション数)
| OFFLINE | SDKの初期化が未完了または失敗
| APPCODEINVALID | アプリケーションキーが間違っている
| TOKENEXPIRED | トークンの期限切れ |

## RakutenAuth
---
RakutenAuth は　楽天のログインに関するAPIを提供しております

| 名前 | 説明 | 例
| --- | --- | ---
| ログインページ表示 | ログインページを表示する | `RakutenAuth.openLoginPage(activity: Activity, requestCode: Int)`
| ログインの結果処理 | ログインの結果を処理  | `RakutenAuth.handleActivityResult(data: Intent?, callback: LoginResultCallback)`
| ログアウト | ログアウトする | `RakutenAuth.logout(callback: LogoutResultCallback)`
| ログインチェック | ログインの状態を確認する | `RakutenAuth.hasUserSignedIn(): Boolean`
| ユーザー名取得　 | 楽天会員の名前を取得 | `RakutenAuth.getUserName(context: Context): String`
| ユーザー情報取得 | ユーザーの楽天ポイントメンバーシップランクを取得する | `RakutenAuth.getUserInfo((success: (userInfo: RakutenAuthUserInfo) -> Unit, failed: (e: RakutenRewardAPIError) -> Unit)`

## LoginResultCallback
ログインのコールバックになります

| 名前 | 説明
| --- | ---
| fun loginSuccess() | ログインが成功した　
| fun loginFailed(e: RakutenRewardAPIError) | ログインが成功した

## LogoutResultCallback
ログアウトのコールバックになります

| 名前 | 説明
| --- | ---
| fun logoutSuccess() | ログアウトが成功した
| fun logoutFailed(e: RakutenRewardAPIError) | ログアウトが失敗した


## API Data
---

### MissionData

| パラメータ名 | 説明 | 例
| --- | --- | ---
| name | ミッション名 | Mission A
| actionCode | アクションコード | ZIJCjBeQBHac8nJa
| iconurl | ミッションアイコンのURL | https://mprewardsdk.blob.core.windows.net/sdk-portal/appCode/actionCode.png
| instruction | ミッションの説明文 | 1日1回プレイする
| condition | ミッションの達成条件 | 毎日10回達成可能
| notificationtype | ミッションのノーティフィケーションタイプ | NONE, BANNER, MODAL, CUSTOM
| point | ミッションのポイント | 10
| enddatestr | ミッションの終了日 <br> 日次の場合 : Today<br> 週次 : 週の終わり<br> 月次 : 月の終わり<br> カスタム : 指定された日時<br> | 20190403
| till | ミッション終了日までの残り日数 | 残り3日
| ext | ミッションのための拡張データ |
| reachedCap | ミッション達成が上限に達したかどうか？ | true
| times | ミッション達成に必要なアクション数 | 3
| progress | 現在のアクションの状態 | 1

### RakutenRewardPointHistory

RakutenRewardPoint インスタンスのリストになります

#### RakutenRewardPoint

| パラメータ名 | 説明
| --- | --- 
| point | ポイント数
| pointdate | ポイント付与月 YYYYMM

### MissionAchievementData
| パラメータ名 | 説明
| --- | --- 
| name | ミッション名 |
| iconurl | アイコンのURL |
| instruction |  ミッションの説明 |
| action | アクションコード(キー) |
| custom | ミッションのノーティフィケーションがカスタムかどうか |
| notificationtype | ミッションのノーティフィケーションタイプ |
| point | ポイント |
| unclaimed | 未獲得ミッション件数 |
| achievedDate | ミッション達成日 |

## API Errors
RakutenRewardAPIError は enum になります

| Enum | 説明
| --- | --- 
| NETWORKERROR | ネットワークエラー(接続失敗)
| APIRESPONSEERROR | ネットワークのレスポンスに問題があった(基本的には起こりません)
| TOKENEMPTY | 	アクセストークンがセットされていない
| SDKNOTACTIVE | SDKが初期化されていません
| TOKENEXPIRE |  アクセストークンの有効期限がきれています <br> アクセストークンをリフレッシュしてください
| UNKNOWN | 不明なエラー(基本的には起こりません)

## Last Failed Method
SDKはアプリケーションでエラーを処理できるようにAPIが失敗した場合にその詳細を提供します  
RakutenReward.lastFailed はダイナミックAPIが失敗した時にそのAPIの情報  (RakutenRewardAPILastCalled)とパラメータを提供いたします  

| 名前 | 説明(関数名)
| --- | --- 
| MEMBERINFO | memberInfo
| LOGACTION | logAction
| GETUNCLAIM | getUnclaimedItems
| POINTHISTORY | getPointHistory
| CLAIM | claim (MissionAchievementData)
| GETMISSIONLIST | getMissions


## RakutenRewardClaimStatus

| Enum | 説明
| --- | --- 
| NOTYET | まだクレイムしていない
| SUCCESS | クレイム成功
| FAIL | クレイム失敗

## ミッションのリストを取得する
```kotlin
RakutenReward.getMissions({ missions ->
            // ミッションを取得できた
        }, {
            // 失敗した
        })
```

## RakutenRewardAdConfiguration
---
こちらの機能は台湾でのみご利用になれます
```kotlin
RakutenRewardAdConfiguration.propertyname
```
| パラメータ名 | 説明 | 例 
| --- | --- | ---
| bcat | 広告のコンテンツをIABのコンテンツに基づきブロックする | RakutenRewardAdConfiguration.bcat
| badv | 広告のドメインレベルでのブロック | RakutenRewardAdConfiguration.badv
| appDomain |  アプリのドメイン(アプリの紹介ページのトップなど) | RakutenRewardAdConfiguration.appDomain
| storeUrl | アプリストアのURL | RakutenRewardAdConfiguration.storeUrl
| privacyPolicy | プライバシーポリシーの有無　 0　= 用意していない、 1 = 用意している | RakutenRewardAdConfiguration.privacyPolicy
| paid | アプリが無料か有料かどうか 0 = 無料、 1 = 有料 | RakutenRewardAdConfiguration.paid
| keywords | アプリのキーワード | RakutenRewardAdConfiguration.keywords
| test | テストモードの切り替え(デバッグ用) | RakutenRewardAdConfiguration.test
<br>

| メソッド | 説明 | 例 
| --- | --- | ---
| addBlockCategory | 広告のコンテンツブロックの対象を追加する<br>フォーマット: IAB(Number)-(Number) | addBlockCategory(str: "IAB7-17")
| addBlockDomain | 広告のドメインレベルでのブロックの対象を追加する | addBlockCategory(str: "www.example.com")
| addKeywords | 広告キーワードを追加する | addKeywords(str: "製品")
<br>

## ミッション達成後のカスタムUIの作り方
SDKのイベントリスナー RakutenRewardListener を使ってミッションの達成イベントを受け取ります　

```kotlin
override fun onUnclaimedAchievement(achievement: MissionAchievementData) {
    if (achievement.custom && RakutenRewardConfig.isUiEnabled()) {
         // 達成通知を表示する
    }
}
```

ポイントを獲得するには、MissionAchievementDataクラスの claim API を使います。
ユーザーに対して達成のノーティフィケーションを見せた後、クレームの処理を上記のAPIを呼び出して行います。

```kotlin
achievement.claim()
```
詳しくは、サンプルアプリケーションの実装などをご覧ください

---
言語 :
> [![en](../../lang/en.png)](../../APIReference/README.md)