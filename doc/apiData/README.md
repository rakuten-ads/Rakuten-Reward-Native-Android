[TOP](../../README.md#top)　> API Data  

Table of Contents  
* [MissionAchievementData](#missionachievementdata)  
* [MissionData](#missiondata)  
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

# API Data  


## MissionAchievementData 
| Property name    | Description                           |
|------------------|---------------------------------------|
| name             | Mission name                          |
| iconurl          | Icon URL                              |
| instruction      | Mission Instruction                   |
| action           | Action code                           |
| custom           | Whether notification is custom or not |
| notificationtype | Notification type                     |
| point            | Point                                 |
| unclaimed        | Number of unclaimed                   |
| achievedDate     | Mission Achieved Date                 |  

---  

## MissionData  

| Property name    | Description                                                                                                                                          | Example                                                                     |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| name             | Mission name                                                                                                                                         | Mission A                                                                   |
| actionCode       | Action code                                                                                                                                          | ZIJCjBeQBHac8nJa                                                            |
| iconurl          | Mission icon URL                                                                                                                                     | https://mprewardsdk.blob.core.windows.net/sdk-portal/appCode/actionCode.png |
| instruction      | Mission Instruction                                                                                                                                  | 1日1回プレイする                                                                   |
| condition        | Mission condition                                                                                                                                    | 毎日10回達成可能                                                                   |
| notificationtype | Mission Notification type                                                                                                                            | NONE, BANNER, MODAL, CUSTOM, BANNER_50, BANNER_250                          |
| point            | Point for this mission                                                                                                                               | 10                                                                          |
| enddatestr       | This mission's end date (String style) <br> Daily : Today<br> Weekly : End of this week<br> Monthly : End of this month<br> Custom : Custom date<br> | 20190403                                                                    |
| till             | The rest days of this mission                                                                                                                        | 残り3日                                                                        |
| ext              | Extension data for mission (future use) Map                                                                                                          |                                                                             |
| reachedCap       | This mission reached achievement limit of today                                                                                                      | true                                                                        |
| times            | Required action times                                                                                                                                | 3                                                                           |
| progress         | Current action progress                                                                                                                              | 1                                                                           |

---

## RakutenRewardPointHistory  
List of `RakutenRewardPoint` data class  

## RakutenRewardPoint  

| Property name | Description             |
|---------------|-------------------------|
| point         | Point data              |
| pointdate     | Point date month YYYYMM |  

---  

## RakutenRewardUser  
RakutenRewardUser is user data class.

| Parameter       | Description                                     |
|-----------------|-------------------------------------------------|
| unclaimed       | Number of unclaim Point Item get from Unclaimed |
| signin          | Whether user is sign or not                     |
| point           | Point the user get from Reward Service          |
| achievementList | Mission list (not use)                          |

---  

## Status  

### RakutenRewardSDKStatus  

| Name             | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| ONLINE           | SDK is ready. SDK Member Information(get point, unclaimed number correctly) |
| OFFLINE          | SDK is not ready. And initialization API is failed                          |
| APPCODEINVALID   | Application Key was invalid. initialization API return 400 (bad request)    |
| TOKENEXPIRED     | APIs returns Token Expired                                                  |
| USER_NOT_CONSENT | User have not provide consent yet (Since v4.0.0)                            |  
---  

<br>

### RakutenRewardClaimStatus

| Enum    | Description           |
|---------|-----------------------|
| NOTYET  | Not claim yet (start) |
| SUCCESS | Succeed to claim      |
| FAIL    | Failed to claim       |  
---  

<br>

### RakutenRewardConsentStatus

| RakutenRewardConsentStatus              | Description                                             |
|-----------------------------------------|---------------------------------------------------------|
| CONSENT_PROVIDED                        | User already provide consent                            |
| CONSENT_NOT_PROVIDED                    | User have not provide consent                           |
| CONSENT_FAILED                          | There is some error with API request                    |
| CONSENT_PROVIDED_RESTART_SESSION_FAILED | User provided consent but failed to restart SDK session |  
---  

<br>

### RewardApiResult
Reward API result which return in `RakutenRewardCoroutine`.  

#### Success  
| Property Name | Description     |
|---------------|-----------------|
| data          | API data object |

#### Failed  
| Property Name | Description             |
|---------------|-------------------------|
| error         | `RakutenRewardAPIError` |  

---  

<br>  

### RakutenRewardAPIError  

| Enum                | Description                                                               |
|---------------------|---------------------------------------------------------------------------|
| NETWORKERROR        | Network connection error                                                  |
| INVALIDREQUEST      | Parameter is invalid                                                      |
| TOKENEMPTY          | Access token is not set                                                   |
| SDKNOTACTIVE        | SDK is not initialized yet                                                |
| TOKENEXPIRE         | Access token expired to access API <br> Need to refresh this access token |
| UNKNOWN             | Unknown error, basically not happen                                       |  
| USER_NOT_CONSENT    | User haven't provide consent                                              |  
| MISSION_REACHED_CAP | Mission achievement already reached cap                                   |  
---  

<br>

### Last Failed Method  
SDK provides information about failed method to handle error easily.  

#### RakutenRewardAPILastCalled  
| Property Name | Description                                    |
|---------------|------------------------------------------------|
| method        | The last failed API in `RakutenRewardAPI` enum |
| parameters    | Parameters for the API call                    |  

#### RakutenRewardAPI enum  

| Name            | Description(method name)       |
|-----------------|--------------------------------|
| MEMBERINFO      | memberInfo                     |
| LOGACTION       | logAction                      |
| GETUNCLAIM      | getUnclaimedItems              |
| POINTHISTORY    | getPointHistory                |
| CLAIM           | claim (MissionAchievementData) |
| GETMISSIONLIST  | getMissions                    |  
| PROVIDE_CONSENT | provideConsent                 |


---
LANGUAGE :
> [![ja](../lang/ja.png)](../ja/apiData/README.md)  
