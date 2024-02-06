# Update History

### Version 5.2.1
<hr/>
Release Date: 2024/02/05

* Bug fix

### Version 5.2.0
<hr/>
Release Date: 2024/01/09

* Remove poikatsu tab in SDK Portal
* Introduce `MISSION_REACHED_CAP` error code [refer here](../core/RakutenReward.md#mission-achievement-reached-cap)
* Minor bug fix

### Version 5.1.0
<hr/>
Release Date: 2023/12/05

* Remove deprecated API
* Minor bug fix

### Version 5.0.0
<hr/>
Release Date: 2023/11/02

* Android 14 (API 34) support
* Remove SDK Core library dependency
* Improve SDK Portal performance
* Update Unclaim info message in SDK Portal

### Version 4.1.0
<hr/>
Release Date: 2023/09/12

* Increase min SDK support to Android 7.0 (API level 24)
* Support Ra cookie set function
* Upgrade to Android Gradle Plugin 7.3.1
* Upgrade to Kotlin 1.6.21

### Version 4.0.0
<hr/>
Release Date: 2023/07/28

* Introduce request user consent feature

### Version 3.7.0
<hr/>
Release Date: 2023/07/14

* SDK Portal UI Update
    * Introduce Unclaimed List sorting feature
    * Tap on mission item to show mission details
* Marked `RakutenReward.openAdPortal()` as deprecated API
* Update [FAQ page](../faq/README.md)

### Version 3.6.0
<hr/>
Release Date: 2023/04/12

* Upgrade to JAVA 11
* Upgrade to Android Gradle Plugin 7.1.0

### Version 3.5.1
<hr/>
Release Date: 2023/03/22

* Bug fix

### Version 3.5.0
<hr/>
Release Date: 2023/02/10

* Introduce Poikatsu in SDK Portal
* Update Claim UI
* Upgrade SDK Core library
* Bug fix

### Version 3.4.2
<hr/>
Release Date: 2022/12/02

* Update mini browser support
* Introduce `RakutenReward.startSession` API
* Provide alternative API which uses Activity Result Callback instead of getting result from `Activity.onActivityResult`
    * `RakutenAuth.openLoginPage`
    * `RakutenReward.openSDKPortal`
    * `RakutenReward.openAdPortal`

### Version 3.4.1
<hr/>
Release Date: 2022/10/25

* Upgrade to Android SDK version API 33
* Rakuten Ichiba App support
* Remove Taiwan Region support
* Bug fix

### Version 3.4.0
<hr/>
Release Date: 2022/09/28

* Upgrade to Android SDK version API 31
* Support new mission achieved notification
* Remove `onBackPressed()` and `KeyEvent.KEYCODE_BACK` usage
* Bug fix

### Version 3.3.0
<hr/>
Release Date: 2022/08/26

* Manual initialization no longer needed. Instead please set your AppCode in AndroidManifest.xml. Please refer [here](../basic/README.md#from-version-330-onward-manual-initialization-is-no-longer-needed).
* Coroutine Support. Please refer [here](../basic/README.md#coroutine-support)
* Rakuten Ichiba App support
* Improve get mission list API validation
* Improve LogAction and Claim API

### Version 3.2.2
<hr/>
Release Date: 2022/07/07

* Update help page URL
* Update claim UI flow in SDK portal
* Upgrade SDK Core library
* Minor bug fix

### Version 3.2.1
<hr/>
Release Date: 2022/06/16

* Upgrade SDK Core library
* Rakuten Ichiba App support

### Version 3.2.0
<hr/>
Release Date: 2022/05/31

* Improve global ad
* Minor UI bug fix
* Improve LogAction API validation
* Fix database access concurrency issue

### Version 3.1.2
<hr/>
Release Date: 2022/05/04

* Display loading icon in claim UI
* Fix Cookie setting
* Rakuten Ichiba App support

### Version 3.1.1
<hr/>
Release Date: 2022/04/08

* Improve LogAction API
* SDK Debug Log feature
* UI bug fix
* Update Log Out API
    * Clients who are using ID SDK or User SDK login options are required to call Log Out API when user log out

### Version 3.1.0
<hr/>
Release Date: 2022/03/07

* Update kotlin version
* Add Event Ananlytics function
* Rakuten Ichiba App support
* Open Ad in external browser feature
* Introduce `RakutenReward.addRakutenRewardListener` and `RakutenReward.removeRakutenRewardListener` to replace deprecated `RakutenReward.listener`

### Version 3.0.0
<hr/>
Release Date: 2022/01/27

* Update SDK portal UI
* Upgrade sdk core library
* Update minimum supported Android version to 21
* Update `RakutenRewardBaseActivity` to extend from `FragmentActivity` instead of `Activity` 

### Version 1.1.4
<hr/>
Release Date: 2022/01/19

* Upgrade to Android SDK version API 30
* Upgrade sdk core library

### Version 2.4.1
<hr/>
Release Date: 2022/01/14

* Improve SDK portal mission icons' memory manangement
* Limit to display maximum 15 unclaim items in SDK Portal
* New openLoginPage API with Fragment reference as argument

### Version 2.4.0
<hr/>
Release Date: 2021/12/29

* Upgrade to Android SDK version API 30
* New Ad Portal feature
* Update deprecated PreferenceManager class to AndroidX PreferenceManager
* Fix logic for openSdkPortal API
* Several bug fixes

### Version 2.3.3
<hr/>
Release Date: 2021/12/02

* Update Traditional Chinese labels
* Display global logo for Taiwan region
* Remove Mission Achievement toggle in SDK Portal

### Version 2.3.2
<hr/>
Release Date: 2021/11/12

* Fix UI problems

### Version 2.3.1
<hr/>
Release Date : 2021/10/11

* Fix lifecycle issue(Add new API)
* Fix logic for openPortal API
* Fix claim API java compatibility

### Version 2.3.0
<hr/>
Release Date : 2021/09/21

* Fix Wall Advertisement issues
* Upgrade Android Development Environment(gradle)
* Add Notification limitaion to show (on SDK Portal)

### Version 1.1.3
<hr/>
Release Date : 2021/08/31

* Upgrade Android Development Environment(gradle)
* Upgrade sdk core library

### Version 2.2.2
<hr/>
Release Date : 2021/07/26

* Fix Android 5 Login Issue

### Version 2.2.1
<hr/>
Release Date : 2021/06/08

* Fix wall advertisement show logic problem

### Version 2.2.0
<hr/>
Release Date : 2021/05/27

* Support Rp, Rz cookie set function
* Provide force close claim flow API
* Support Coupon Advertisements
* Fix data sync issue when the user logout

### Version 2.1.0
<hr/>
Release Date : 2021/03/01

* Support Taiwan Region

### Version 2.0.0
<hr/>
Release Date : 2020/09/28

* Support 3rd party login (external login)

### Version 1.1.2
<hr/>
Release Date : 2020/11/23

* Add advertisement loading icon
* Fix UI problems(text)

### Version 1.1.1
<hr/>
Release Date : 2020/10/20  

* Upgrade Android SDK version API 29

### Version 1.1.0
<hr/>
Release Date : 2020/06/18  

* Support User SDK (now ID SDK with RAE)

### Version 1.0.0
<hr/>
Release Date : 2020/02/20  

* First version

---
Language :
> [![ja](../lang/ja.png)](../ja/history/README.md)