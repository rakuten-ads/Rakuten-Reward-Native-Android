[TOP](../../README.md#top) > SPS feature

Table of Contents
* [Overview](#overview)
* [Import SPS library](#import-sps-library)
* [Enable SPS feature](#enable-sps-feature)
* [Authentication](#authentication)
    * [ID SDK](#id-sdk)
* [Initialize SPS](#initialize-sps)
* [Show SPS Portal](#show-sps-portal)
* [Claim Point Screen](#claim-point-screen)
* [Theme Setting Screen](#theme-setting-screen)
* [Maintenance Screen](#maintenance-screen)
* [Google Interstitial Ad](#google-interstitial-ad)
* [Migration Guide](#migration-guide)
    * [7.2.0](#migrate-to-720)

---  

# Overview  
Mission SDK provides a new feature which integrate Super Point Screen (SPS) Ad.  

# Import SPS Library  
Add maven repository to the settings.gradle or project-level build.gradle  
**settings.gradle**
```groovy
dependencyResolutionManagement {
    repositories {
        // ...
        maven { url 'https://artifactory.rakuten-it.com/sps-android-sdk-mvn-release/' }
    }
}
```  
**build.gradle**
```groovy  
allprojects {
    repositories {
        // ...
        maven { url 'https://artifactory.rakuten-it.com/sps-android-sdk-mvn-release/' }
    }
}
```

Then add the SPS dependency to the app-level build.gradle file  
```groovy
dependencies {
  // Import the BoM for the Reward Native platform
  implementation platform('com.rakuten.android:rewardsdknative-bom:x.x.x')

  // Mandatory libraries to support SPS library
  implementation 'com.rakuten.android:rewardsdknative-core' 
  implementation 'com.rakuten.android:rewardsdknative-ui' 

  // Declare the library for SPS feature
  implementation 'com.rakuten.android:rewardsdknative-sps' 
}
```  

# Enable SPS feature
In order to use the SPS feature in Mission SDK, please ask SPS BU to enable the feature for your application.  

# Authentication  
Due to Mission SDK and SPS have different system for authentication, so we can't share the same token among two SDKs.  
Please follow the instruction below according to the authentication options the client app is using.  

## Login Option
SPS feature is required to use Rakuten ID SDK. Please check with the developer team for the neccessary configuration update.    
<br>  

# Initialize SPS  
Initialize SPS feature with the following API  
```kotlin
RakutenMissionSps.init("platform-name") {
    // request exchange token
    ...
    SpsCompatToken.CatExchange(tokenValue = exchangeToken)
}
```  
Please check with SPS team regarding the `platform-name`.  

# Show SPS Portal  
The following API will display SPS Portal as shown below.   
<img src="img/sps_osusume.png" alt="SPS Osusume Ad" width="250">  

```kotlin
RakutenReward.openSpsPortal("<rzCookie>", { result ->
   when (result) {
      is Failed -> // Failed to open Portal. Get the error here `result.error`
      is Success -> // SDK Portal opened successfully
  }
}) {
    // handle portal closed event
}
```  
Below are the possible error code returned
| RakutenRewardAPIError | Reason |
| --- | --- |
| `USER_NOT_CONSENT` | User declines the consent dialog, or cancels the SPS member registration screen |
| `NOTSUPPORT` | SPS feature is not enabled for this app (please contact the SDK team) |
| `UNDER_MAINTENANCE` | SPS feature is under maintenance |
| `NETWORKERROR` | Network error while checking SPS membership |
| `SDKNOTACTIVE` | SDK is opted out |
| `INVALIDREQUEST` | No Activity reference available to open the portal. Please refer [here](../basic/README.md#to-start-sdk-in-your-activity-we-provide-several-ways) to start the SDK session in your Activity |

***Since 7.3.0 rz cookie parameter is added to `openSpsPortal` for better personalized experience in the portal***  

Screenshots of the SPS Portal  

<img src="img/sps_portal_home.png" alt="SPS Home Page" width="250">  <img src="img/sps_portal_mission.png" alt="Mission Page" width="250">  

## Campagin Deeplink
<details>
<summary>Expand</summary>

***Since 8.3.0 deeplink URL parameter is added to `openSpsPortal` to open a specific page.***

```kotlin
RakutenReward.openSpsPortal(
    rz = "<rzCookie>",
    deeplink = "<deeplinkURL>",
    isPortalOpenedCallback = { result ->
        when (result) {
            is Failed -> // Failed to open Portal. Get the error here `result.error`
            is Success -> // SDK Portal opened successfully
        }
    },
    activityResultCallback = {
        // handle portal closed event
    }
)
```

</details>

## Non-SPS member
If the logged in user is not a SPS member, a member registration screen will be shown first.  

<img src="img/sps_registration.png" alt="SPS member registration" width="250">  

# Claim Point Screen  
Importing this SPS library will update the Claim Point screen as well.  
Below is a screenshot of the new screen.  
<img src="img/sps_claim_view.png" alt="Claim Point screen" width="250">   

# Theme Setting Screen
In the SPS Portal settings screen, users are able to set their desire theme.   
<img src="img/sps_mode_settings.png" alt="Mode Settings Screen" width="250">  
Currently we support 2 themes: 
| Mission Theme |
| --- |
| Panda |
| Simple |

If your application also provide theme options and would like to sync the selected theme, you can implement the listener to SDK.    
```kotlin
RakutenMissionSps.setSpsMissionListener(object: SpsMissionListener {
    override fun onThemeChanged(theme: MissionTheme) {
        // it will be triggered when user changed the theme in the Mode settings screen
    }
})
```  

You can call the following API to sync the theme setting from your application to Mission SDK.  
```kotlin
// set to Okaimono Panda theme
RakutenRewardConfig.setTheme(MissionTheme.Panda)

// or set to Simple theme
RakutenRewardConfig.setTheme(MissionTheme.Simple)
```  

# Opt Out Mission Feature  
If your application is not intended to use any mission features, use the following API to opt out of mission features.  
```kotlin  
// set true to opt out. By default the value is false
RakutenRewardConfig.setOptOutMissionFeatures(true)
```  
<img src="img/opt-out-mission-dialog-jp.png" alt="Opt Out Mission Feature Dialog" width="250">  
  

# Maintenance Screen 
Since v7.4.0 when SPS service is under maintenance, users will not be able to access the SPS feature and a maintenance page will be shown. 

<img src="img/saas_maintenance.png" alt="SaaS Maintenance Page" width="250">


<br/>

# Google Interstitial Ad

The SDK supports showing a Google Interstitial Ad after a user earns a point from the SPS landing page. This is an optional feature backed by a separate module — if the module is not included, the SDK behaves as before with no ad shown.

## How it works

When a user completes a point-earning action in the SPS landing page:
1. The SDK checks whether an interstitial ad provider is registered.
2. If a provider is registered, a full-screen loading indicator is displayed while the ad is being prepared.
3. Once the ad is ready, it is displayed as a full-screen interstitial.
4. After the ad is dismissed, the SDK pre-loads the next ad silently in the background.

If no provider is registered (i.e. the `rewardsdknative-ads` module is not included), steps 2–4 are skipped entirely.

## Integration steps

### 1. Add the `rewardsdknative-ads` dependency

```groovy
dependencies {
    implementation 'com.rakuten.android:rewardsdknative-ads'
}
```

No further initialisation code is required. The module registers itself automatically at app startup via a `ContentProvider`.

### 2. Set up Google Mobile Ads SDK

Follow the official Google integration guide to complete the required setup in your app:
https://developers.google.com/admob/android/quick-start

> ⚠️ This step is mandatory. The interstitial ad will not work if the Google Mobile Ads SDK is not properly set up.

### 3. Configure the ad unit ID on the backend

Contact the dev team to configure the ad unit ID for your platform on the backend.

---

# Migration Guide  
## Migrate to 7.2.0  
In version 7.2.0, `RakutenMissionSps` class is refactored to be `object` class. So `RakutenMissionSps.INSTANCE` variable is not available anymore.  
| AS-IS | TO-BE |
|---|---|
| RakutenMissionSps.INSTANCE.setPlatform() | RakutenMissionSps.setPlatform() |
| RakutenMissionSps.INSTANCE.setSpsMissionListener() | RakutenMissionSps.setSpsMissionListener() |
| RakutenMissionSps.INSTANCE.setLocation() | RakutenMissionSps.setLocation() |  
