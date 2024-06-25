[TOP](../../README.md#top)　> Core API  

Table of Contents  
* [RakutenReward](#rakutenreward)  
* [RakutenRewardCoroutine](#rakutenrewardcoroutine)  
* [RakutenAuth](#rakutenauth)  
* [RakutenRewardConfig](#rakutenrewardconfig)  

---  

# Core API  
## RakutenReward  
`RakutenReward` class provides main settings and main functions of Reward SDK.  
Refer [here](./RakutenReward.md) for the available API.  

<br>  

## RakutenRewardCoroutine  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
`RakutenRewardCoroutine` class provide API in suspend function.  

| API Name                                                | Description                      |
|---------------------------------------------------------|----------------------------------|
| [getMissions](./RakutenReward.md#mission-list)          | Get missions                     |
| [getPointHistory](./RakutenReward.md#point-history)     | Get 3 month user's point history |
| [logAction](./RakutenReward.md#post-mission-action)     | Post user action                 |
| [getUnclaimedItems](./RakutenReward.md#unclaimed-items) | Get Unclaim item list            |
| [memberInfo](./RakutenReward.md#member-informations)    | Get the latest member info       |  

These API return [`RewardApiResult`](../apiData/README.md#rewardapiresult) which is either `Success` or `Failed`.  

```kotlin
val result = RakutenRewardCoroutine.memberInfo()
when (result) {
    is Success -> {
        result.data // api data
    }
    is Failed -> {
        result.error // error code
    }
}
```  

<br>  

## RakutenAuth  
`RakutenAuth` class provides login and logout functions and access to basic user information.  

| API Name                                                                     | Description                                                                               | 
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [openLoginPage](../basic/LOGIN.md#1-show-login-page)                         | Open Log In page                                                                          |
| [handleActivityResult](../basic/LOGIN.md#2-get-result-from-onactivityresult) | Parse activity result from login page                                                     | 
| [hasUserSignedIn](../basic/UserInfo.md#check-if-user-is-signed-in)           | Check if user is logged in with internal system (token not expired)                       |
| [logout](../basic/README.md#log-out)                                         | Log out from Rakuten Auth, you might force removing session even if server sync up failed | 
| [getUserName](../basic/UserInfo.md#get-users-full-name)                      | Get Rakuten Member name                                                                   |
| [getUserInfo](../basic/UserInfo.md#get-users-current-point-and-rank)         | Load latest point & rank from server                                                      |  

<br>  

## RakutenRewardConfig
`RakutenRewardConfig` is user settings class.  

| API Name         | Description                                                                    | 
|------------------|--------------------------------------------------------------------------------|
| isOptedOut       | Get Optout status <br><b>true</b> : Optout (Reward SDK function does not work) |
| setOptedOut      | Set Optout status                                                              | 
| isUiEnabled      | Get whether Notification UI is enabled or not                                  | 
| setUiEnabled     | Set whether Notification UI is enabled or not                                  |
| isDebuggable     | Set Reward SDK to be debuggable                                                | 
| isUsingSdkPortal | Set whether using SDK Portal or not (only available in UI module)              |  

<br>  

---
LANGUAGE :
> [![ja](../lang/ja.png)](../ja/core/README.md)

