[TOP](../../README.md#top)　>　Event Analytics

Table of Contents
* [Event Analytics function Overview](#event-analytics-function-overview)
* [Import Event Analytics Module](#import-event-analytics-module)
* [Enable Event Analytics function](#enable-event-analytics-function)
* [Convert Analytics SDK Event to Mission Event](#convert-analytics-sdk-event-to-mission-event)

---
# Event Analytics function Overview
Mission SDK provides new function named "Event Analytics" with Analytics SDK.<br>
This function main purpose is to enhance App Event Analysis function + Encourage Mission SDK use.<br>
We provide following function<br>
* Can see Event Analytics Dashboard in Mission SDK Dashboard (Enhance App Event Analytics)
* Convert Analytics SDK Event to Mission Event

# Import Event Analytics Module
To use Event Analytics function, please import following module
```groovy
implementation 'com.rakuten.android:rewardsdknative-event:1.1.0'
```
At the same time, Analytics SDK is required to import <br>
Please check [Rakuten Analytics SDK for Android](https://github.com/rakutentech/android-analytics)

# Enable Event Analytics function
Set enable Event Analytics feature

```kotlin
RakutenRewardConfig.setMissionEventFeatureEnabled(true)
```

# Convert Analytics SDK Event to Mission Event
This is new function with Analytics SDK<br>
Developers can set Event Mapping data using developer portal<br>

## Use Case
* At first, add Analytics Event to your app (analysis purpose event) with Event Analytics API (mission SDK)
* If you want to add this event as incentive mission, you can switch Mission SDK Event in Developer Portal
* After switch, this Event becomes both Analytics SDK and Mission SDK event

This is new API to realize this 
```kotlin
RakutenMissionEvent.logAction("actionname", mapOf(), {
   // Success
}, {
   // Failed
})
```

If you need meta data for Analytics SDK, please use
```kotlin
var map = mutableMapOf<String, Object>()
map["key"] = "value" as Object
RakutenMissionEvent.logAction("actionname", map, {}, {})
```

※ This actionname is Analytics SDK Action name, not Mission SDK actionCode

This API works
* If mission conversion is missing, send Analytics SDK Event 
* If mission conversion setting exists in Mission SDK Dashboard (Analytics SDK action name ↔  Mission actioncode mapping),  Send both event Analytics SDK and Mission SDK


---
言語 :
> [![ja](../lang/ja.png)](../ja/EventAnalytics/README.md)
