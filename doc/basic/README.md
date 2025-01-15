[TOP](../../README.md#top)　>　Basic Guide

Table of Contents
* [Authentication](#authentication)<br>
  * [Login Options](#login-options)<br>
  * [Log in](#log-in)<br>
  * [Log out](#log-out)<br>
* [Initialize SDK](#initialize-sdk)<br>
* [SDK Status](#sdk-status)<br>
* [User Information](#user-information)<br>
* [Mission Achievement](#mission-achievement)<br>
* [SDK Built-in UI](#sdk-built-in-ui)<br>
* [SDK Debugging Log](#sdk-debugging-log)<br>
* [Coroutine Support](#coroutine-support)<br><br>

---
# Authentication

## Login Options
There are 3 types of login. According to your environment, please select proper one. 
<br>

| Login Option | Description                                                                             |
|--------------|-----------------------------------------------------------------------------------------|
| RakutenAuth  | This is default option, provide login by SDK, SDK handled all login and user identifier |
| RID          | Rakuten ID SDK with RID, Login covers by ID SDK, and use API token for SDK              |  
| RAE          | Rakuten ID SDK with RAE, Login covers by User SDK, and use token for SDK                |
<br>

## Switch Login Option
By default, login option is RakutenAuth
<br>

### RakutenAuth
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
To use SDK API, need to set API (API-C) token by developers  

```kotlin
RakutenReward.setRIdToken("token")
```

For login implementation, please read ID SDK login documentation.

> :grey_exclamation:  **From version 3.1.1, developers require to call logout API whenever user log out to properly clear token and data**

Refer to [Log Out](#log-out)  

<br>

### RAE
```kotlin
RakutenReward.tokenType = RakutenRewardTokentype.RAE
```
<details>
    <summary>JAVA</summary>

```java
RakutenReward.INSTANCE.setTokenType(RakutenRewardTokentype.RAE);
```    
</details>
To use SDK API, need to set access API token by developers  

```kotlin
RakutenReward.setRaeToken("token")
```

For login implementation, please read User SDK login documentation.

> :grey_exclamation:  **From version 3.1.1, developers require to call logout API whenever user log out to properly clear token and data**

Refer to [Log Out](#log-out)  

<br>

# Log in
Refer [here](./LOGIN.md) to show login page.  
If you use Rakuten Login SDK, you don't need to use this option.  

<br>  


# Log out
Logging user out.  
> Developers require to call this API whenever user log out regardless of login options to properly clear token and data.  

```kotlin
private fun logout() {
    RakutenAuth.logout(object : LogoutResultCallback {
        override fun logoutSuccess() {
            //logout completed
        }

        override fun logoutFailed(e: RakutenRewardAPIError) {
            //login failed
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
        //logout completed
    }

    @Override
    public void logoutFailed(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {
        //logout failed
    }
});
```    
</details>  

<br>

# Initialize SDK
## Initialize SDK in your Application class with your `App Code`.
```kotlin
class App: Application() {

    override fun onCreate() {
        super.onCreate()
        //init sdk with your App Code
        RakutenReward.init("<AppCode>")
    }
}
```

| Parameter name | Description                                                    |
|----------------|----------------------------------------------------------------|
| AppCode        | Application Key (This is from Rakuten Reward Developer Portal) |

If you use RAE, RID option, you need to set token to activate SDK.
<br/><br/>

### **\*From version 3.3.0 onward, manual initialization is no longer needed.**
Set your `App Code` in your application's AndroidManifest.xml as follow:
```xml
<application>
    <!-- Reward SDK Application Key -->
    <meta-data
        android:name="com.rakuten.gap.ads.mission_core.appKey"
        android:value="{Application Key}"/>
</application>
```

<br>

## To start SDK in your Activity, we provide several ways:

### Option 1. Extends RakutenRewardBaseActivity
```kotlin
class YourActivity : RakutenRewardBaseActivity() {}
```
(If you are not able to extend RakutenRewardBaseActivity, use method 2 and 3)
### Option 2. Call Lifecycle Method in each Android Lifecycle
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

### Option 3. Call AndroidX base lifecycle method
```kotlin
class YourActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        RakutenRewardManager.bindRakutenRewardIn(this, this)
    }
}
```  

<br>

# SDK Status  
In order to use the API, need to ensure SDK Status is switched to ONLINE first.   
There are 2 ways to get the SDK status: 

## RakutenReward.status  
Directly access `RakutenReward.status` to get the current SDk Status.  

## RakutenRewardListener  
Add [`RakutenRewardListener`](../core/RakutenReward.md#rakutenrewardlistener) to get notified when SDK status has changed.  
```kotlin  
RakutenReward.addRakutenRewardListener(object : RakutenRewardListener {
    override fun onSDKStatusChanged(status: RakutenRewardSDKStatus) {
        if (status == RakutenRewardSDKStatus.ONLINE) {
            // SDK status is ONLINE
        }
    }
})
```  
***Note: If using [Option 1](#option-1-extends-rakutenrewardbaseactivity), then don't have to add RakutenRewardListener. You can directly override the method.***


# User Information  
Refer [here](./UserInfo.md) for the available API.  
> These API are eligible for `RAKUTEN_AUTH` login options only.   

<br>

# Mission Achievement 
Refer [here](./MissionAchivement.md) to achieve a mission.  

<br>

# SDK Built-in UI  
Refer [here](./SdkPortal.md) for the available UI.  

<br>

# SDK Debugging Log  
[![support version](http://img.shields.io/badge/core-3.1.1+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220408_v3_1_1)  
SDK provide an option to enable SDK debugging logs. Use the following API in your Application class.
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

**It's recommended to enable the debug log in DEBUG mode only**

After enable the debug log, you can see the SDK logs with the tag `RakutenRewardSDK`.  

<br>

# Coroutine Support  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
SDK provide API in suspend function.
The suspend function API are available in `RakutenRewardCoroutine`. Please refer [here](../APIReference/README.md#rakutenrewardcoroutine) for the available API.

Please call the suspend function API in a Coroutine Scope, for eg. `viewModelScope` or `lifecycleScope`.
```kotlin
lifecycleScope.launch { 
    // call the API in a Coroutine scope
    val result = RakutenRewardCoroutine.getMissions()
    when (result) {
        is Failed -> {
            // error case
            result.error // error code
        }
        is Success -> {
            // success case
            val missionList = result.data
        }
    }
}
```  
<br>

---
LANGUAGE :
> [![ja](../lang/ja.png)](../ja/basic/README.md)
