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
  implementation platform('com.rakuten.android:rewardsdknative-bom:6.0.0')

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
RakutenReward.openSpsPortal({ result ->
   when (result) {
      is Failed -> // Failed to open Portal. Get the error here `result.error`
      is Success -> // SDK Portal opened successfully
  }
}) {
    // handle portal closed event
}
```  
Screenshots of the SPS Portal  

<img src="img/sps_portal_home.png" alt="SPS Home Page" width="250">  <img src="img/sps_portal_mission.png" alt="Mission Page" width="250">  

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
RakutenMissionSps.INSTANCE.setSpsMissionListener(object: SpsMissionListener {
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
