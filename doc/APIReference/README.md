[TOP](../../README.md#top)　> API Reference

Table of Contents
* [RakutenReward](#rakutenreward)<br>
* [RakutenRewardCoroutine](#rakutenrewardcoroutine)<br>
* [RakutenAuth](#rakutenauth)<br>
* [Rakuten Reward Config](#rakutenrewardconfig)<br>
* [Open Reward Web Page](#open-reward-web-page)<br>
* [RakutenRewardUser](#rakutenrewarduser)<br>
* [RakutenAuthUserInfo](#rakutenauthuserinfo)
* [Rank](#rank)<br>
* [RakutenRewardListener](#rakutenrewardlistener)<br>
* [RakutenRewardStatus](#rakutenrewardstatus)<br>
* [RakutenAuth](#rakutenauth)<br>
* [LoginResultCallback](#loginresultcallback)<br>
* [LogoutResultCallback](#logoutresultcallback)<br>
* [API Data](#api-data)<br>
  * [MissionData](#missiondata)<br>
  * [RakutenRewardPointHistory](#rakutenrewardpointhistory)<br>
  * [RakutenRewardPoint](#rakutenrewardpoint)<br>
  * [MissionAchievementData](#missionachievementdata)<br>
* [API Errors](#api-errors)<br>
* [Last Failed Method](#last-failed-method)<br>
* [RakutenRewardClaimStatus](#rakutenrewardclaimstatus)<br>
* [Get current user action status](#get-current-user-action-status)<br>
* [How to create custom mission UI](#how-to-create-custom-mission-ui)<br>
* [Set Rakuten cookie](#set-rakuten-cookie)<br>
* [Close Claim UI by back button](#close-claim-ui-by-back-button)<br><br>

# API Reference
## RakutenReward
---
RakutenReward class is to provide main settings and main functions of Reward SDK  

| API Name | Description | Example
| --- | --- | ---
| Get version |  Get Rakuten Reward SDK Version | `RakutenReward.version`
| Open SDK Portal | Open SDK Portal | `RakutenReward.openSDKPortal()`
| Open Ad Portal | Open Ad Portal | `RakutenReward.openAdPortal(activity: Activity, reqCode: Int)`
| Open Help Page | Open Reward SDK Help page with mini browser | `RakutenReward.openHelpPage()`
| Open Terms and Condition Page | Open Reward SDK Terms and Conditions Page with mini browser | `RakutenReward.openTCPage()`
| Open Privacy Policy Page | Open Reward SDK Privacy Policy Page with mini browser | `RakutenReward.openPrivacyPage()`
| Get Missions | Get missions | `RakutenReward.getMissions( { missions -> <br> // Get Missions <br> }, { // Failed<br> })`
| Get Point history | Get 3 month user's point history | `RakutenReward.getPointHistory({ pointHistory -> <br> // Get Point History <br> }, { <br> // Failed <br>})`
| Log Action | Post user action | `RakutenReward.logAction("xxxxxx", { <br> // Success <br>}, { <br> // Failed <br>})`
| Get Unclaimed Items | Get Unclaim item list | `RakutenReward.getUnclaimedItems({ missions -> <br> // Unclaim Mission List <br> }, { <br>// Error <br>})`
| Last failed method | Get last failed method | `RakutenReward.lastFailed`
| Close Claim flow UI | Close Claim flow UI forcibly | `RakutenReward.forceClaimClose()`
| Set Rp cookie | Set Rp cookie from App |  `RakutenReward.setRp(rp: String)`
| Set Rz cookie | Set Rz cookie from App |  `RakutenReward.setRz(rz: String)`
| Add RakutenRewardListener | Add RakutenRewardListener |  `RakutenReward.addRakutenRewardListener(listener)`
| Remove RakutenRewardListener | Remove RakutenRewardListener |  `RakutenReward.removeRakutenRewardListener(listener)`
| Start Session | Start SDK Session | `RakutenReward.startSession()`


## RakutenRewardCoroutine
---
`RakutenRewardCoroutine` class provide API in suspend function

| API Name | Description | Example
| --- | --- | ---
| Get Missions | Get missions | `RakutenRewardCoroutine.getMissions()`
| Get Point history | Get 3 month user's point history | `RakutenRewardCoroutine.getPointHistory()`
| Log Action | Post user action | `RakutenRewardCoroutine.logAction("xxxxxx")`
| Get Unclaimed Items | Get Unclaim item list | `RakutenRewardCoroutine.getUnclaimedItems()`


## RakutenAuth
---
| API Name | Description | Example |
| --- | --- | --- |
| Log In | Open Log In page | `RakutenAuth.openLoginPage(activity: Activity, requestCode: Int)` |
| Log In | Open Log In page | `RakutenAuth.openLoginPage(fragment: androidx.fragment.app.Fragment, requestCode: Int)` |
| Check Log In | Check if user is logged in with internal system (token not expired)  | `RakutenAuth.hasUserSignedIn()` |
| Log Out |  Log out from Rakuten Auth, you might force removing session even if server sync up failed  | `RakutenAuth.logout(object : LogoutResultCallback)` |
| Get Rakuten Member name | Get Rakuten Member name | `RakutenAuth.getUserName()` |
| Get Rakuten Point & Rank | Load latest point & rank from server  | `RakutenAuth.RakutenAuth.getUserInfo(success = { userInfo <br>-> <br>}, {<br> // Error <br>})` |

## RakutenRewardConfig
RakutenRewardConfig is user setting class.

| API Name | Description | Example 
| --- | --- | ---
| Get Optout | Get Optout status <br>true : Optout (Reward SDK function does not work) | `RakutenRewardConfig.isOptedOut()`
| Set Optout | Set Optout status | `RakutenRewardConfig.setOptedOut(true)`
| isUiEnabled |  Get whether Notification UI is enabled or not | `RakutenRewardConfig.isUiEnabled()`
| setUiEnabled | Set whether Notification UI is enabled or not | `RakutenRewardConfig.setUiEnabled(true)`
| isDebuggable | Set Reward SDK to be debuggable | `RakutenRewardConfig.isDebuggable()`

## Open Reward Web page
---
SDK provide page open with API  

Help Page
```kotlin
RakutenReward.openHelpPage()
```
Terms and Condition Page  
```kotlin
RakutenReward.openTCPage()
```
Privacy Policy
```kotlin
RakutenReward.openPrivacyPage()
```

## RakutenRewardUser
---
RakutenRewardUser is user data class.

| Parameter | Description |
| --- | ---
| unclaimed | Number of unclaim Point Item get from Unclaimed
| signin | Whether user is sign or not
| point | Point the user get from Reward Service
| achievementList | Mission list (not use)

## RakutenAuthUserInfo
---
User info available for Rakuten Auth

| Parameter | Description
| --- | ---
| points | Total Rakuten points of an user
| rank | User's Rakuten account rank

### Rank
---
This is only for Japan

| Rank | Description |
| --- | ---
| 1 | Regular |
| 2 | Silver |
| 3 | Gold |
| 4 | Platinum |
| 5 | Diamond |

## RakutenRewardListener
---
RakutenRewardListener is Rakuten Reward SDK basic function status change listener

| Name | Description
| --- | ---
| fun onUnclaimedAchievement(achievement : MissionAchievementData) | When the user achieved the mission
| fun onUserUpdated(user : RakutenRewardUser) | When the user data is updated
| fun onSDKStatusChanged(status : RakutenRewardSDKStatus) | When the SDK status changed
| fun onSDKClaimClosed(missionAchievementData: MissionAchievementData, status: RakutenRewardClaimStatus) | When the claim UI closed

For usage, please take a look sample application codes.


### RakutenRewardSDKStatus
---
RakutenRewardSDKStatus is Reward SDK Status  

| Name | Description
| --- | ---
| ONLINE | SDK is ready. SDK Member Information(get point, unclaimed number correctly)
| OFFLINE | SDK is not ready. And initialization API is failed
| APPCODEINVALID | Application Key was invalid. initialization API return 400 (bad request)
| TOKENEXPIRED | APIs returns Token Expired

## RakutenAuth
---
RakutenAuth class provides login and logout functions and access to basic user information.

| API Name | Description | Example
| --- | --- | ---
| Open Login Page |  Start and show login page | `RakutenAuth.openLoginPage(activity: Activity, requestCode: Int)`
| Handle Activity Result | Parse activity result from login page  | `RakutenAuth.handleActivityResult(data: Intent?, callback: LoginResultCallback)`
| Logout | Log user out | `RakutenAuth.logout(callback: LogoutResultCallback)`
| Has User Logged In | Check if user has logged in with Rakuten Auth | `RakutenAuth.hasUserSignedIn(): Boolean`
| Get User Name | Get Rakuten Auth user's full name | `RakutenAuth.getUserName(): String`
| Get User Info | Get user's points and rank | `RakutenAuth.getUserInfo((success: (userInfo: RakutenAuthUserInfo) -> Unit, failed: (e: RakutenRewardAPIError) -> Unit)`

## LoginResultCallback
---
Login result callback for RakutenAuth login

| Name | Description
| --- | ---
| fun loginSuccess() | Login completed
| fun loginFailed(e: RakutenRewardAPIError) | Login failed with error

## LogoutResultCallback
---
Logout result callback for RakutenAuth

| Name | Description
| --- | ---
| fun logoutSuccess() | Logout completed
| fun logoutFailed(e: RakutenRewardAPIError) | Logout failed with error
<br>

## API Data
---
We provide some API which supports to create own custom UI for Reward SDK
API list are in RakutenReward class

### MissionData

| Property name | Description | Example
| --- | --- | ---
| name | Mission name | Mission A
| actionCode | Action code | ZIJCjBeQBHac8nJa
| iconurl | Mission icon URL | https://mprewardsdk.blob.core.windows.net/sdk-portal/appCode/actionCode.png
| instruction | Mission Instruction | 1日1回プレイする
| condition | Mission condition | 毎日10回達成可能
| notificationtype | Mission Notification type | NONE, BANNER, MODAL, CUSTOM, BANNER_50, BANNER_250
| point | Point for this mission | 10
| enddatestr | This mission's end date (String style) <br> Daily : Today<br> Weekly : End of this week<br> Monthly : End of this month<br> Custom : Custom date<br> | 20190403
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
| INVALIDREQUEST | Parameter is invalid  
| TOKENEMPTY | 	Access token is not set
| SDKNOTACTIVE | SDK is not initialized yet
| TOKENEXPIRE |  Access token expired to access API <br> Need to refresh this access token
| UNKNOWN | Unknown error, basically not happen

## Last Failed Method
SDK provides information about Failed method to handle error easily.  
RakutenRewardAPILastCalled class has API information and parameters  
RakutenRewardAPI is enum class

| Name | Description(method name)
| --- | --- 
| MEMBERINFO | memberInfo
| LOGACTION | logAction
| GETUNCLAIM | getUnclaimedItems
| POINTHISTORY | getPointHistory
| CLAIM | claim (MissionAchievementData)
| GETMISSIONLIST | getMissions

## RakutenRewardClaimStatus

| Enum | Description
| --- | --- 
| NOTYET | Not claim yet (start)
| SUCCESS | Succeed to claim
| FAIL | Failed to claim

## Get current user action status
```kotlin
RakutenReward.getMissions({ missions ->
            // Get misson
        }, {
            // Failed
        })
```

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
achievement.claim({}, {})
```
For detail, please check sample application implementation

## Set Rakuten cookie 
This function can be used from SDK v2.2.0
This function is mainly for Rakuten App and use cookies which app keeps in App  
If you use default login option(RakutenRewardTokentype.RAKUTEN_AUTH), cookie is set by SDK.  
If you use other options, can override cookie using this API  

### Set Rp cookie
```kotlin
RakutenReward.setRp("cookie")
```

### Set Rz cookie
```kotlin
RakutenReward.setRz("cookie")
```

## Close Claim UI by back button
By default, claim UI does not close by Android back button  
So, if the user press Android back button, only Activity is closed  
If you use RakutenRewardBaseActivity, already implement this function by default.  
In other cases, SDK Provide API to close Claim UI.  

```kotlin
RakutenReward.forceClaimClose()
```
Please call this API by application

---
LANGUAGE :
> [![ja](../lang/ja.png)](../ja/APIReference/README.md)