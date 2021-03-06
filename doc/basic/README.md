[TOP](../../README.md#top)　>　Basic Guide

Table of Contents
* [Region Setting](#region-setting)<br>
* [Authentication](#authentication)<br>
  * [Login Options](#login-options)<br>
  * [Log in](#log-in)<br>
  * [Log out](#log-out)<br>
* [Initialize SDK](#initialize-sdk)<br>
* [Getting User Information](#getting-user-information)<br>
* [Mission Achievement](#mission-achievement)<br>
* [SDK Portal](#sdk-portal)<br><br>

---
# Region Setting
From Version 2.1, SDK support multiple regions.
We support Japan, Taiwan(2021/02).

For Japan
```kotlin
RakutenRewardConfig.region = RakutenRewardRegion.JP
```

For Taiwan
```kotlin
RakutenRewardConfig.region = RakutenRewardRegion.TW
```

Do not use multiple setting in same app.  
We expect one application use one region.  
Each Region has differrent functions, and we cannot support each country mixed.

# Authentication

## Login Options
There are 3 types of login. According to your environment, please select proper one. 
<br>

| Login Option        | Description | Support |
| --- | --- | --- |
| RakutenAuth | This is default option, provide login by SDK, SDK handled all login and user identifier | Japan, Taiwan |
| RID | Rakuten ID SDK with RID, Login covers by ID SDK, and use API token for SDK| Japan |  
| RAE | Rakuten ID SDK with RAE, Login covers by ID SDK, and use token for SDK | Japan |
<br>

### Switch Login Option
By default, login option is RakutenAuth
<br>

### RakutenAuth
```kotlin
RakutenReward.tokenType = RakutenRewardTokentype.RAKUTEN_AUTH
```
<br>

### RID
```kotlin
RakutenReward.tokenType = RakutenRewardTokentype.RID
```
To use SDK API, need to set API)(API-C) token by developers  
```kotlin
RakutenReward.setRIdToken("token")
```

For login implementation, please read SDK login documentation.

### RAE
```kotlin
RakutenReward.tokenType = RakutenRewardTokentype.RAE
```

To use SDK API, need to set access API token by developers
```kotlin
RakutenReward.setRaeToken("token")
```

For login implementation, please read SDK login documentation.

# Log in
### 1. Show Login Page
This is for external login options,
If you use Rakuten Login SDK, you don't need to use this option.

```kotlin
RakutenAuth.openLoginPage(context, REQUEST_THIRD_PARTY_LOGIN)
```

### 2. Get result from `onActivityResult()`
```kotlin
override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if (requestCode == REQUEST_THIRD_PARTY_LOGIN) {
            if (resultCode == RESULT_OK) {
                handleActivityResult(data)
            } else {
                //login canceled by user
            }
        }
    }
```

### 3. Process result intent to complete login flow by calling `RakutenAuth.handleActivityResult()`
```kotlin
private fun handleActivityResult(data: Intent?) {
        RakutenAuth.handleActivityResult(data, object : LoginResultCallback {
            override fun loginSuccess() {
                //✅ login completed
            }

            override fun loginFailed(e: RakutenRewardAPIError) {
                //⛔ login failed
            }
        })
    }
```

![Login](Login.jpg)


# Log out
Logging user out: 

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


# Initialize SDK
### Initialize SDK in your Application class with your `App Code`.
```kotlin
class App: Application() {

    override fun onCreate() {
        super.onCreate()
        //init sdk with your App Code
        RakutenReward.init(this, "<AppCode>")
    }
}
```

| Parameter name        | Description           
| --- | --- 
| AppCode | Application Key (This is from Rakuten Reward Developer Portal)

If you use RAE, RID option, you need to set token to activate SDK.

<br><br/>
### To start SDK in your Activity, we provide several ways:

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

---
# Getting user information

List of available api to retrieve user information

## Check if user is signed in
```kotlin
RakutenAuth.hasUserSignedIn(): Boolean
```

## Get user's full name
```kotlin
RakutenAuth.getUserName(context: Context): String
```

## Get user's current point and rank
```kotlin
RakutenAuth.getUserInfo(
    success = { userInfo ->
        //get point
        userInfo.points
        
        //get rank
        userInfo.rank
    }, 
    failed = {
        //fail to get user info
    }
)
```
---
# Mission Achievement 
To achieve mission, developers need to call post action API.  
After avhieving the mission, notification will be shown.  

## Post Action
```kotlin
RakutenReward.logAction("<actionCode>", {}, {})
```
actionCode is provided by Reward SDK Developer Portal.  

## Notification UI
The user achieved the mission, notification UI is shown.  
Reward SDK provides Modal and Banner UI

![Modal](Modal.jpeg)     ![Banner](Banner.jpeg)

### Notification Type
There  are 4 types of Mission Achievement UI. Modal, Banner, and No UI, and Custom which developed by developers.

You can decide type by Developer Portal 

| Notification Type        | UI
| --- | ---
| Modal | Show Modal UI provided by SDK
| Banner | Show Banner UI provided by SDK
| Custom | Developer can create UI by themselves
| No UI | Not show any UI

## SDK Portal
We provide User Portal UI for developers. To call Open SDK Portal API, developers can see user status (mission, unclaim list, current point, point history etc...)

```kotlin
RakutenReward.openSDKPortal()
```

This is UI Image

![Portal1](Portal1.png)

![Portal2](Portal2.png)

![Portal3](Portal3.png)

![Portal4](Portal4.png)

![Portal5](Portal5.png)

---
LANGUAGE :
> [![ja](../lang/ja.png)](../ja/basic/README.md)
