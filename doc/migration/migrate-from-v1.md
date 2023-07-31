[TOP](../../README.md#top)　>　Migration Guide: Migrate from V1 SDK

Table of Contents
* [Background](#background)
* [Integration Guide](#integration-guide)
   * [Update Dependency](#update-dependency)
   * [Data Binding feature](#data-binding-feature)
   * [Android Gradle Plugin](#android-gradle-plugin)
* [API Changes](#api-changes)
   * [Update Package Name](#update-package-name)
   * [SDK Initialization](#sdk-initialization)
   * [Set Token](#set-token)
   * [Clear Token](#clear-token)
   * [Deprecated methods](#deprecated-methods)
* [New Features](#new-features)
   * [SDK Debugging Log](#sdk-debugging-log)
   * [Coroutine Support](#coroutine-support)
   * [New Notification Type](#new-notification-type)
   * [User Consent Feature](#user-consent-feature)

---

# Background
V1 SDK is a legacy SDK, starting from V2 there are a lot of significant changes. This document provide a guide on how to migrate from V1 SDK and the changes required.

This document will also share some new features introduced since V2.  

# Integration Guide

## Update Dependency
Update the dependency name in app-level `build.gradle` file.  
If your app is using Reward SDK built-in UI, for eg: `RakutenReward.openSDKPortal()`, please update the dependency name to the following:
```groovy
implementation 'com.rakuten.android:rewardsdknative-ui:4.0.0'
```
**For latest version please refer to [version history](../history/README.md)**

If your app don't use Reward SDK built-in UI, please update the dependency name to the following:
```groovy
implementation 'com.rakuten.android:rewardsdknative-core:4.0.0'
```

## Data Binding feature
`rewardsdknative-ui` uses data binding and view binding, please enable the binding features in `app/build.gradle` file if your app never enabled it before.
```groovy
android {
   // ...
   buildFeatures {
        viewBinding true
        dataBinding true
   }
}
```  

## Android Gradle Plugin 
Since version 3.6.0, Reward SDK has upgrade Android Gradle Plugin (AGP) to 7.1  
Please upgrade your application's AGP to version 7.0 or later.
<br/><br/>


# API Changes
## Update Package Name
Most Reward SDK classes name remain the same as V1 in newer versions. However the package name are different.  
In your classes which uses Reward SDK's API, please update the import package name from
```kotlin
import com.rakuten.gap.ads.rakutenrewardnative.api.RakutenReward
```
to  
```kotlin
import com.rakuten.gap.ads.mission_core.RakutenReward
```
**Hint: Use Android Studio global replace to replace `com.rakuten.gap.ads.rakutenrewardnative.api` to `com.rakuten.gap.ads.mission_core`**  

There are some classes may still have error after replacing the package name, please use Android Studio's helper import to import the correct class package.
For eg: `RakutenReward.openSDKPortal()` need to import the following
```groovy
import com.rakuten.gap.ads.mission_ui.api.activity.openSDKPortal
```

## SDK Initialization
* Set your `AppKey` in the application's AndroidManifest.xml
```xml
<application>
    <!-- Reward SDK Application Key -->
    <meta-data
        android:name="com.rakuten.gap.ads.mission_core.appKey"
        android:value="{Application Key}"/>
</application>
```
* Remove the following `init` method from your code
```kotlin
RakutenReward.init("<AppKey>", "<Token>")
```

## Set Token
* `RakutenReward.token` is no longer available. To set the token to SDK please use the following API:  
```kotlin
// for RID login option
RakutenReward.setRIdToken("token")

// for RAE login option
RakutenReward.setRaeToken("token")
```
Please refer [here](../basic/README.md#login-options) for the login option to use.  

## Clear Token
* You cannot access `RakutenReward.token` anymore, so to clear the token or when user logout please use the following API to clear the data:
```kotlin
RakutenAuth.logout(object : LogoutResultCallback {
      override fun logoutSuccess() {
         //logout completed
      }

      override fun logoutFailed(e: RakutenRewardAPIError) {
         //logout failed
      }
   })
```


## Deprecated methods
The following methods which require `Context` as parameter is deprecated in version 3.3.0. Replace these methods with the new API by removing the context argument.
* `RakutenRewardConfig.setOptedOut(context, optedOut)`
* `RakutenRewardConfig.setUiEnabled(context, uiEnabled)`
<br/><br/>


`RakutenReward.listener` variable is deprecated , please use the following API to provide the listener instance.

**NOTE: If your Activity class is extended from `RakutenRewardBaseActivity`, you don't need to provide `RakutenRewardListener` instance as this is already handled by `RakutenRewardBaseActivity` class. You can simply override the listener methods in your Activity class**

* To set `RakutenRewardListener` instance
```kotlin
override fun onResume() {
    super.onResume()
    RakutenReward.addRakutenRewardListener(listener)
}
```

* Call the following API to remove the listener instance to avoid memory leak
```kotlin
override fun onPause() {
    super.onPause()
    RakutenReward.removeRakutenRewardListener(listener)
}
```  
<br/><br/>

# New Features
## SDK Debugging Log
Since v3.1.1, SDK provide an option to enable SDK debugging logs. Use the following API in your Application class.
```kotlin
override fun onCreate() {
    if (BuildConfig.DEBUG) {
        RakutenRewardConfig.isDebuggable()
    }
}
```  
After enable the debug log, you can see the SDK logs with the tag `RakutenRewardSDK`.

## Coroutine Support
Since v3.3.0, SDK provide API in suspend function.  
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

## New Notification Type  
There are 2 new mission achieved notification types added since v3.4.0.  
* Small Ad Banner
* Big Ad Banner  

![Small Ad Banner](../basic/AdBannerSmall.png)     ![Big Ad Banner](../basic/AdBannerBig.png)  


## User Consent Feature
In Reward SDK V4, we added support for User Consent feature where user have to provide consent before accessing Rewards Service.  
Please refer [here](../consent/README.md) for more details.  

**\* Currently this feature is not enabled yet**

![Consent Dialog](../consent/consent-dialog.png)  

