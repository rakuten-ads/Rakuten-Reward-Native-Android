[TOP](../../README.md#top)　>　Migration Guide

Table of Contents
* [Migration to version 3.3.0](#migrate-to-version-x00)
    * [SDK Initialization](#sdk-initialization)
    * [Deprecated Methods](#deprecated-methods)
* [Migrate to version 3.1.0](#migrate-to-version-310)
---
# Migrate to version 3.3.0
### SDK Initialization
* Set your `AppCode` in the application's AndroidManifest.xml
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
RakutenReward.init(context, "<AppCode>")
```

#### For RAE, RID login options
* Remove the following `init` method if you are using it
```kotlin
RakutenReward.init("<AppCode>", "<Token>")
```
* Set token with the following API:
```kotlin
// for RID login option
RakutenReward.setRIdToken("token")

// for RAE login option
RakutenReward.setRaeToken("token")
```
<br/>

### Deprecated methods
The following methods which require `Context` as parameter is deprecated in version 3.3.0. Replace these methods with the new API by removing the context argument.
* `RakutenAuth.getUserName(context)`
* `RakutenRewardConfig.setOptedOut(context, optedOut)`
* `RakutenRewardConfig.setUiEnabled(context, uiEnabled)`

<br/><br/>

# Migrate to version 3.1.0
`RakutenReward.listener` variable is deprecated in version 3.1.0. Use the following API to provide the listener instance.

**NOTE: If your Activity class is extended from `RakutenRewardBaseActivity`, you don't need to provide `RakutenRewardListener` instance as this is already handled by `RakutenRewardBaseActivity` class. You can simple override the listener methods in your Activity class**

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

---
LANGUAGE :
> [![ja](../lang/ja.png)](../ja/migration/README.md)