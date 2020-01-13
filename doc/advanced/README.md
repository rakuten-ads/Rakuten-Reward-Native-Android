[TOP](../../README.md#top)　> Advanced Guide

---
# Advanced Integration Guide
## RakutenReward
RakutenReward class is to provide main settings and main functions of Reward SDK  

| API Name | Description | Example
| --- | --- | ---
| Get version |  Get Rakuten Reward SDK Version | RakutenReward.version
| Open SDK Portal | For detail, please check sample application implementation | RakutenReward.openSDKPortal()
| Open Help Page | Open Reward SDK Help page with mini browser | RakutenReward.openHelpPage()
| Open Terms and Condition Page | Open Reward SDK Terms and Conditions Page with mini browser | RakutenReward.openTCPage()
| Open Privacy Policy Page | Open Reward SDK Privacy Policy Page with mini browser | RakutenReward.openPrivacyPage()
| Get Missions | Get missions | RakutenReward.getMissions( { missions -> <br> // Get Missions <br> }, { // Failed<br> })
| Get Point history | Get 3 month user's point history | RakutenReward.getPointHistory({ pointHistory -> <br> // Get Point History <br> }, { <br> // Failed <br>})
| Log Action | Post user action | RakutenReward.logAction("xxxxxx")
| Get Unclaimed Items | Get Unclaim item list | RakutenReward.getUnclaimedItems({ missions -> <br> // Unclaim Mission List <br> }, { <br>// Error <br>})

## RakutenRewardConfig
RakutenRewardConfig is user setting class.

| API Name | Description | Example 
| --- | --- | ---
| Get Optout | Get Optout status <br>true : Optout (Reward SDK function does not work) | RakutenRewardConfig.isOptedOut()
| Set Optout | Set Optout status | RakutenRewardConfig.setOptedOut(context, true)
| isUiEnabled |  Get whether Notification UI is enabled or not | RakutenRewardConfig.isUiEnabled()
| setUiEnabled | Set whether Notification UI is enabled or not | RakutenRewardConfig.setUiEnabled(context, true)

## RakutenRewardUser
RakutenRewardUser is user data class.

| Parameter | Description |
| --- | ---
| unclaimed | Number of unclaim Point Item get from Unclaimed
| signin | Whether user is sign or not
| point | Point the user get from Reward Service
| achievementList | Mission list (not use)

## RakutenRewardListener
RakutenRewardListener is Rakuten Reward SDK basic function status change listener

| Name | Description
| --- | ---
| fun onUnclaimedAchievement(achievement : MissionAchievementData) | When the user achieved the mission
| fun onUserUpdated(user : RakutenRewardUser) | When the user data is updated
| fun onSDKStatusChanged(status : RakutenRewardSDKStatus) | When the SDK status changed
| fun onSDKClaimClosed(missionAchievementData: MissionAchievementData, status: RakutenRewardClaimStatus) | When the claim UI closed

For usage, please take a look sample application codes.

## API Data
We provide some API which supports to create own custom UI for Reward SDK
API list are in RakutenReward class

### MissionData

| Property name | Description | Example
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

List of RakutenRewardPoint data class

#### RakutenRewardPoint

| Property name | Description
| --- | --- 
| point | Point data
| pointdate | Point date month YYYYMM

### MissionAchievementData
| Property name | Description
| --- | --- 
| name | Mission name |
| iconurl | Icon URL |
| instruction | Mission Instruction |
| action | Action code |
| custom | Whether notification is custom or not |
| notificationtype | Notification type |
| point | Point |
| unclaimed | Number of unclaimed |
| achievedDate | Mission Achieved Date |

## API Errors
RakutenRewardAPIError enum class

| Enum | Description
| --- | --- 
| NETWORKERROR | Network connection error
| APIRESPONSEERROR | Failed API response was collapsed, not happen basically
| TOKENEMPTY | 	Access token is not set
| SDKNOTACTIVE | SDK is not initialized yet
| TOKENEXPIRE |  Access token expired to access API-C <br> Need to refresh this access token
| UNKNOWN | Unknown error, basically not happen

## RakutenRewardClaimStatus

| Enum | Description
| --- | --- 
| NOTYET | Not claim yet (start)
| SUCCESS | Succeed to claim
| FAIL | Failed to claim

## How to support custom view after mission achievement
Use RakutenRewardListener to receive mission achievement callback

```kotlin
override fun onUnclaimedAchievement(achievement: MissionAchievementData) {
    if (achievement.custom && RakutenRewardConfig.isUiEnabled()) {
         // Show UI
    }
}
```
To claim point using API, please call claim API provided by MissionAchievementData class

After show UI, we need to handle claim for user

```kotlin
achievement.claim()
```
For detail, please check sample application implementation

---
LANGUAGE :
> [![ja](../lang/ja.png)](../ja/advanced/README.md)