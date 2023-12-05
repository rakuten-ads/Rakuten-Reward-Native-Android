[TOP](/README.md#top)　>　[Core API](./README.md)　>  RakutenReward  

Table of Contents  
* [Properties](#properties)  
* [Public Methods](#public-methods)  
  * [RakutenRewardListener](#rakutenrewardlistener)  
  * [Mission List](#mission-list)  
  * [Point History](#point-history)  
  * [Unclaimed Items](#unclaimed-items)  
  * [Init API](#init-api)  
  * [Post Mission Action](#post-mission-action)  
  * [Member Informations](#member-informations)  
  * [Open Reward Web Page](#open-reward-web-page)  
  * [Set Rakuten Cookie](#set-rakuten-cookie)  
  * [Request for Consent](#request-for-consent)  
  * [Start SDK Session](#start-sdk-session)  

---  
# RakutenReward
RakutenReward class provides main settings and main functions of Reward SDK.  

## Properties  
| Property Name | Description                |
|---------------|----------------------------|
| appCode       | Reward SDK Application Key |
| [lastFailed](../apiData/README.md#last-failed-method)    | The last failed API call   |
| status        | Reward SDK status          |
| tokenType     | Switch ID solution         |
| user          | User Data                  |
| version       | Reward SDK version         |  

<details>
    <summary>JAVA</summary>

In JAVA, to access the property value please use the `get` method.  

Example  
```java 
RakutenReward.INSTANCE.getAppCode();
```  

</details>  

<br>

## Public Methods  
| Method Name                 | Description                                              |
|-----------------------------|----------------------------------------------------------|
| [addRakutenRewardListener](#rakutenrewardlistener)    | Add Event Listener                                       |
| clearAccessToken            | Clear Access Token                                       |
| forceClaimClose             | Close claim UI forcibly                                  |
| [getMissions](#mission-list)| Get the mission list                                     |
| [getPointHistory](#point-history)| Get user's last 3 months point history                   |
| [getUnclaimedItems](#unclaimed-items)| Get the list of unclaimed items                          |
| [init](#init-api)           | Initialize Reward SDK                                    |
| [logAction](#post-mission-action)| Post a mission action                                    |
| [memberInfo](#member-informations)| Get the latest member info                               |
| [openHelpPage](#open-reward-web-page)| Open Rakuten Reward Help Page                            |
| [openPrivacyPage](#open-reward-web-page)| Open Rakuten Reward Privacy Policy Page                  |
| [openTCPage](#open-reward-web-page)| Open Rakuten Reward T&C Page                             |
| [removeRakutenRewardListener](#rakutenrewardlistener) | Remove Event Listener                                    |
| [requestForConsent](#request-for-consent)           | Request for consent if user have not provide consent yet |
| [setRa](#set-rakuten-cookie)| Set Ra cookie                                            |
| setRaeToken                 | Set RAE Token                                            |
| setRidToken                 | Set RID Token                                            |
| [setRp](#set-rakuten-cookie)| Set Rp cookie                                            |
| [setRz](#set-rakuten-cookie)| Set Rz cookie                                            |
| [startSession](#start-sdk-session)                | Start SDK session                                        |  

### RakutenRewardListener
RakutenRewardListener is Rakuten Reward SDK basic function status change listener.  

| Name                                                                                                   | Description                        |
|--------------------------------------------------------------------------------------------------------|------------------------------------|
| fun onUnclaimedAchievement(achievement : MissionAchievementData)                                       | When the user achieved the mission |
| fun onUserUpdated(user : RakutenRewardUser)                                                            | When the user data is updated      |
| fun onSDKStatusChanged(status : RakutenRewardSDKStatus)                                                | When the SDK status changed        |
| fun onSDKClaimClosed(missionAchievementData: MissionAchievementData, status: RakutenRewardClaimStatus) | When the claim UI closed           |
| fun onSDKConsentClosed                                                                                 | When consent dialog is closed (Since v4.0.0)|  
<br>

**To add the listener**  
[![support version](http://img.shields.io/badge/core-2.4.1+-green.svg?style=flat)](/doc/history//README.md#version-310)  

```kotlin
RakutenReward.addRakutenRewardListener(this)
```  

> If this method is used in Activity or Fragment class, please call the remove API whenever Activity class is destroyed to prevent memory leak.  

**To remove the listener**   
[![support version](http://img.shields.io/badge/core-2.4.1+-green.svg?style=flat)](/doc/history//README.md#version-310)  

```kotlin
RakutenReward.removeRakutenRewardListener(this)
```  

Please refer [here](/doc/faq/README.md#how-do-i-implement-onsdkstatuschanged-or-onunclaimedachievement) for more information.  

<br>  

### Mission List  
The following API return a list of [`MissionData`](../apiData/README.md#missiondata) object.  

Kotlin  
```kotlin
RakutenReward.getMissions({ missions ->
    // get missions success
}) {
    // get missions failed
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

Coroutine  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
```kotlin
val result : RewardApiResult<List<MissionData>> = RakutenRewardCoroutine.getMissions()
```  

<br>

### Point History  
The following API return a [`RakutenRewardPointHistory`](../apiData/README.md#rakutenrewardpointhistory) object.  

Kotlin  
```kotlin
RakutenReward.getPointHistory({ pointHistory ->
    // success
}, {
    // error
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

Coroutine  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
```kotlin
val result : RewardApiResult<RakutenRewardPointHistory> = RakutenRewardCoroutine.getPointHistory()
```   

<br>  

### Unclaimed Items  
The following API return a list of [`MissionAchievementData`](../apiData/README.md#missionachievementdata) objects.  

Kotlin  
```kotlin
RakutenReward.getUnclaimedItems({ unclaimed ->
    // success
}) {
    // error
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

Coroutine  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
```kotlin
val result : RewardApiResult<List<MissionAchievementData>> = RakutenRewardCoroutine.getUnclaimedItems()
```   

<br>  

### Init API  
Initialize SDK  

> Since **3.3.0**, these API are deprecated due to manual initialization is no longer needed. Refer [here](../basic/README.md#from-version-330-onward-manual-initialization-is-no-longer-needed) for more information.  

```kotlin
RakutenReward.init("<appCode>")
```  

| Parameter name | Description                                                    |
|----------------|----------------------------------------------------------------|
| AppCode        | Application Key (This is from Rakuten Reward Developer Portal) |  

**For RID, RAE login options**  
You can provide access token in the init API.  
```kotlin
RakutenReward.init("<appCode>", "<token>")
```  

<br>  

### Post Mission Action  
The following API post a mission action.  

Kotlin
```kotlin
RakutenReward.logAction("actionCode", {
    // post action success
}) {
    // post action failed
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

Coroutine  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
```kotlin
val result : RewardApiResult<Unit> = RakutenRewardCoroutine.logAction("actionCode")
```   

<br>  

### Member Informations
The following API return a [`RakutenRewardUser`](../apiData/README.md#rakutenrewarduser) object  

Kotlin  
```kotlin
RakutenReward.memberInfo({ user ->
    // success
}) {
    // error
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

Coroutine  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
```kotlin
val result : RewardApiResult<RakutenRewardUser> = RakutenRewardCoroutine.memberInfo()
```   

<br>  

### Open Reward Web Page  
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

<br>  

### Set Rakuten Cookie
These API is mainly for Rakuten App and use cookies which app keeps.  
If you use default login option (`RAKUTEN_AUTH`), cookie is handled by Reward SDK.  
If you use other options, you can override cookie using these API.  

**Set Rz Cookie**  
```kotlin
RakutenReward.setRz("cookie")
```  

**Set Rp Cookie**  
```kotlin
RakutenReward.setRp("cookie")
```

**Set Ra Cookie**  
[![support version](http://img.shields.io/badge/core-4.1.0+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20230912_v4.1.0)  
```kotlin
RakutenReward.setRa("cookie")
```

<br>  

### Request for Consent  
[![support version](http://img.shields.io/badge/core-4.0.0+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20230728_v4.0.0)  
Request for consent if the user have not provide consent.  

If user have not provide consent, Consent Dialog will be shown to ask for user's consent.  
Else the callback will be triggered immediately with `CONSENT_PROVIDED` statue. Refer [here](../consent/README.md#request-user-consent-api) for more information.    

The callback return [`RakutenRewardConsentStatus`](../apiData/README.md#rakutenrewardconsentstatus).  

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

### Start SDK Session  
[![support version](http://img.shields.io/badge/core-3.4.2+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20221202_v3_4_2)  
Manually start SDK session.  When SDK is ONLINE, `onSDKStatusChanged` will be triggered.   

```kotlin
RakutenReward.startSession()
```

---
LANGUAGE :
> [![ja](../lang/ja.png)](../ja/core/RakutenReward.md)

