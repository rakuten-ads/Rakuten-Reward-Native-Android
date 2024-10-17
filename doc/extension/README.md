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

## Supported API
Currently this extension library support the following APIs:
* `RakutenReward.logAction`
* `RakutenReward.openSDKPortal`  
* `RakutenReward.openSpsPortal`

In order for the API to work well, start the SDK session in the Activity or the parent Activity if the WebView page is in Fragment.  
[Refer here](../basic/README.md#to-start-sdk-in-your-activity-we-provide-several-ways)

---
LANGUAGE :
> [![jp](../lang/ja.png)](../ja/extension/README.md)  
