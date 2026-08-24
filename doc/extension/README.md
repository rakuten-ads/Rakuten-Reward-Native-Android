[TOP](../../README.md#top) > Extension  

# JavaScript Extension    
In native application there would be some pages where the page is web-based and display in a native WebView. This library is built for the usecase where SDK API to be triggered from a webpage. 

# SDK Setup
This guide focus on the integration in Android. Please refer [here](https://github.com/rakuten-ads/Rakuten-Reward-JS/tree/main/js-extension-library) for the implementation guide on JavaScript.   

## Import SDK  
Add the following to the module build.gradle to import the SDK  

```groovy
    // Import the BoM for the Reward Native platform
    implementation platform('com.rakuten.android:rewardsdknative-bom:x.x.x')
    // ... other library
    implementation 'com.rakuten.android:rewardsdknative-ext'
```  

## Initialization  
Call the following API to initialize this feature:  

```kotlin  
RewardJS.setupWebView("<appCode>", "<domain>", webView)
```  
| Parameter | Desc |
| --- | --- |
| appCode | Application Key (This is from Rakuten Reward Developer Portal) |
| domain | The domain of the webpage where `missionsdk-ext` is implementated |
| webView | The WebView instance which load the webpage |  

In order for the API to work well, start the SDK session in the Activity or the parent Activity if the WebView page is in Fragment.  
[Refer here](../basic/README.md#to-start-sdk-in-your-activity-we-provide-several-ways)

---

## Consent Handling (Since 2.1.1)

Since 2.1.1, if the user has not yet accepted the Reward Terms of Service, any API call will automatically show the consent dialog before proceeding. The API only executes if the user accepts. If the user declines, the API call is not executed.

---

## Supported API

| API | Description |
| --- | --- |
| `logAction(appKey, actionCode)` | Log a mission action |
| `logAction(appKey, actionCode, callback)` | Log a mission action with result callback |
| `openSdkPortal(appKey)` | Open the Reward SDK portal |
| `openSdkPortal(appKey, callback)` | Open the Reward SDK portal with result callback |
| `openSpsPortal(appKey)` | Open the SPS portal |
| `openSpsPortal(appKey, callback)` | Open the SPS portal with result callback |
| `getUserRewardPoint(appKey, callback)` | Get the user's current reward point balance |
| `getPointHistory(appKey, callback)` | Get the user's point history |
| `getMissionLite(appKey, callback)` | Get the mission list (lite version, no progress) |
| `getMissionDetails(appKey, actionCode, callback)` | Get full details of a single mission including progress |
| `getUnclaimList(appKey, callback)` | Get the list of unclaimed mission achievements |
| `claimMissionPoint(appKey, actionCode, achievedDate, callback)` | Claim the point for a mission achievement |

---

## Version Mapping

| BOM   | JS |
|-------| --- |
| 8.2.1 | 1.3.0 |
| 7.6.0 | 1.2.0 |
| 7.5.0 | 1.1.0 |
| 6.2.0 | 1.0.0 |

---

LANGUAGE :
> [![jp](../lang/ja.png)](../ja/extension/README.md)  
