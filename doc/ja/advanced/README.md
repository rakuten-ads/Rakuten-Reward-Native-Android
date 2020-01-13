[TOP](../README.md#top)　> 応用ガイド

---
# 応用ガイド
## RakutenReward
RakutenReward クラスはリワードSDKのメインの設定や機能を提供しています

| API 名 | 説明 | 使用例
| --- | --- | ---
| バージョンの取得 |  リワードSDKのバージョンを取得する | RakutenReward.version
| SDK ポータルを開く | For detail, please check sample application implementation | RakutenReward.openSDKPortal()
| ヘルプページを開く | ヘルプページをSDKのミニブラウザーで開く | RakutenReward.openHelpPage()
| 利用規約を開く | 利用規約をSDKのミニブラウザーで開く | RakutenReward.openTCPage()
| プライバシーポリシーを開く | プライバシーポリシーをDKのミニブラウザーで開く | RakutenReward.openPrivacyPage()
| ミッションリストを取得する | ミッションリストを取得する | RakutenReward.getMissions( { missions -> <br> // Get Missions <br> }, { // Failed<br> })
| ポイント履歴を取得する | 3ヶ月前までのポイント履歴を取得する | RakutenReward.getPointHistory({ pointHistory -> <br> // Get Point History <br> }, { <br> // Failed <br>})
| アクションを送信する | ミッションを達成するためにアクションを送信する | RakutenReward.logAction("xxxxxx")
| 未獲得ミッションを取得する | 未獲得ミッションリストを取得する | RakutenReward.getUnclaimedItems({ missions -> <br> // Unclaim Mission List <br> }, { <br>// Error <br>})

## RakutenRewardConfig
RakutenRewardConfig　はユーザー設定を管理するクラスです

| API 名 | 説明 | Example 
| --- | --- | ---
| オプトアウトの取得 | オプトアウトの状態を取得する <br>true : オプトアウト (リワードSDKは動作しません) | RakutenRewardConfig.isOptedOut()
| オプトアウトの設定 | オプトアウトの状態を設定する | RakutenRewardConfig.setOptedOut(context, true)
| UI設定の取得 |  ミッションのUIのオン・オフ設定設定を取得する | RakutenRewardConfig.isUiEnabled()
| UI設定 | ミッションのUIのオン・オフ設定 | RakutenRewardConfig.setUiEnabled(context, true)

## RakutenRewardUser
RakutenRewardUser ユーザデータのクラスです

| パラメータ名 | 説明 |
| --- | ---
| unclaimed | 未獲得ミッションの数
| signin | 　ユーザーがサインインしているかどうか？
| point | リワードサービスで取得したポイント
| achievementList | ミッションリスト(使用していない)

## RakutenRewardListener
RakutenRewardListener 楽天リワードのイベントに関するリスナーです

| パラメータ名 | 説明
| --- | ---
| fun onUnclaimedAchievement(achievement : MissionAchievementData) | ユーザーがミッションを達成した　
| fun onUserUpdated(user : RakutenRewardUser) | ユーザーデータが更新された
| fun onSDKStatusChanged(status : RakutenRewardSDKStatus) | SDKの状態が変更された
| fun onSDKClaimClosed(missionAchievementData: MissionAchievementData, status: RakutenRewardClaimStatus) | クレイムUIが閉じた

## API Data

### MissionData

| パラメータ名 | 説明 | 例
| --- | --- | ---
| name | Mission name | Mission A
| actionCode | Action code | ZIJCjBeQBHac8nJa
| type | Mission type (DAILY, WEEKLY, MONTHLY, CUSTOM) | DAILY
| iconurl | Mission icon URL | https://mprewardsdk.blob.core.windows.net/sdk-portal/appCode/actionCode.png
| instruction | Mission Instruction | 1日1回プレイする
| condition | Mission condition | 毎日10回達成可能
| notificationtype | Mission Notification type | NONE, BANNER, MODAL, CUSTOM
| point | Point for this mission | 10
| enddatestr | This mission's end date (String style) <br> Daily : Today<br> Weekly : End of this week<br> Monthly : End of this month<br> Monthly : End of this month<br> | 20190403
| till | The rest days of this mission | 残り3日
| ext | Extension data for mission (future use) Map |
| reachedCap | This mission reached achievement limit of today | true
| times | Required action times | 3
| progress | Current action progress | 1

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
| custom | Whether notification is custom or not |
| notificationtype | Notification type |
| point | Point |
| unclaimed | Number of unclaimed |
| achievedDate | Mission Achieved Date |

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

## RakutenRewardClaimStatus

| Enum | 説明
| --- | --- 
| NOTYET | まだクレイムしていない
| SUCCESS | クレイム成功
| FAIL | クレイム失敗

## ミッション達成後のカスタムUIの作り方
SDKのイベントリスナー RakutenRewardListener を使ってミッションの達成イベントを受け取ります　

```kotlin
override fun onUnclaimedAchievement(achievement: MissionAchievementData) {
    if (achievement.custom && RakutenRewardConfig.isUiEnabled()) {
         // Show UI
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
> [![en](../../lang/en.png)](../../advanced/README.md)