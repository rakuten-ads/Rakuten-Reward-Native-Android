[TOP](../../README.md#top)　> Java App Developers

Table of Contents
* [For Java Developers](#for-java-developers)<br>
* [Mission-Java Module](#mission-java-module)<br>
* [How to access API](#how-to-access-api)<br>
* [Properties](#properties)<br/>
* [Callback Kotlin](#callback-kotlin)<br/>
* [Callback Java Style](#callback-java-style)<br><br>

---
# For Java Developers
This SDK is written by Kotlin.<br/>
For Java developers, we provide a dedicated mission-java module with Java-friendly APIs.<br/>

## Mission-Java Module
For Java projects, we recommend using the **mission-java** module which provides clean, Java-friendly APIs without requiring Kotlin syntax knowledge.

### Dependency
Add the mission-java dependency to your app's build.gradle:
```gradle
implementation 'com.rakuten.gap:rewardsdknative-java'
```

### Import
```java
import com.rakuten.gap.ads.mission_java.RakutenRewardJava;
import com.rakuten.gap.ads.mission_java.listeners.*;
```

## How to access API
### RakutenReward
RakutenReward class is object in Kotlin, need to call INSTANCE
```java
RakutenReward.INSTANCE.init("<Appcode>");
```
From SDK 2.3.0, INSTANCE is not required.
```java
RakutenReward.init("<Appcode>");
```

### RakutenReward.openSDKPortal()
This is kotlin extension on mission-ui.<br/>
To access this from Java, need to use Extension call<br/>

```java
RakutenRewardExtensionKt.openSDKPortal(RakutenReward.INSTANCE);
```
From SDK 2.4.0, boolean value is returned
```java
boolean success = RakutenRewardExtensionKt.openSDKPortal(RakutenReward.INSTANCE);
boolean success = RakutenRewardExtensionKt.openSDKPortal(RakutenReward.INSTANCE, <requestCcode>);
```

## Properties
Kotlin can access property directory but in Java case, need to call
using getXxx and setXxx

```java
String version = RakutenReward.INSTANCE.getVersion();

RakutenReward.INSTANCE.setTokenType(RakutenRewardTokentype.RID);
```

## Callback Kotlin
Use Kotlin and Lambda.</br>
If you want to use Kotlin Unit, please import kotlin standard library. (Add Kotlin to an existing app)[https://developer.android.com/kotlin/add-kotlin]<br/>
```java
RakutenReward.INSTANCE.logAction("", () -> { return Unit.INSTANCE; }, (RakutenRewardAPIError e) -> { return Unit.INSTANCE; });
```
This requires Kotlin standard library.<br/>
To call lambda Kotlin callback, required Kotlin Standard library.<br/>

## Callback Java Style
We provide Java friendly callback style APIs through the mission-java module.<br/>

### RakutenRewardJava
The RakutenRewardJava class provides clean Java APIs without "Java" suffixes.<br/>
#### logAction
```java
RakutenRewardJava.logAction("action_code", new LogActionCallback() {
    @Override
    public void success() {
        
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

#### memberInfo
```java
RakutenRewardJava.memberInfo(new MemberInfoCallback() {
    @Override
    public void success(@NonNull RakutenRewardUser rakutenRewardUser) {
        
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```


#### getMissions
```java
RakutenRewardJava.getMissions(new GetMissionsCallback() {
    @Override
    public void success(@NonNull List<MissionData> list) {
        
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

#### getUnclaimedItems
```java
RakutenRewardJava.getUnclaimedItems(new UnclaimedItemCallback() {
    @Override
    public void success(@NonNull List<MissionAchievementData> list) {
        
    }

    @Override
    public void failed(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

#### getPointHistory
```java
RakutenRewardJava.getPointHistory(new PointHistoryCallback() {
    @Override
    public void success(@NonNull RakutenRewardPointHistory rakutenRewardPointHistory) {

    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

#### getMissionsLite
```java
RakutenRewardJava.getMissionsLite(new GetMissionsLiteCallback() {
    @Override
    public void success(@NonNull List<MissionLiteData> list) {
        
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

#### getMissionDetails
```java
RakutenRewardJava.getMissionDetails("action_code", new GetMissionDetailsCallback() {
    @Override
    public void success(@NonNull MissionData mission) {
        
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

#### requestForConsent
```java
// With callback
RakutenRewardJava.requestForConsent(new RequestForConsentCallback() {
    @Override
    public void onRequestConsentResult(@NonNull RakutenRewardConsentStatus status) {

    }
});

// Without callback
RakutenRewardJava.requestForConsent();
```

#### showConsentBanner
```java
// With callback
RakutenRewardJava.showConsentBanner(new RequestForConsentCallback() {
    @Override
    public void onRequestConsentResult(@NonNull RakutenRewardConsentStatus status) {

    }
});

// Without callback
RakutenRewardJava.showConsentBanner();
```

#### getUserInfo
```java
RakutenRewardJava.getUserInfo(new AuthMemberInfoCallback() {
    @Override
    public void success(@NonNull RakutenAuthUserInfo rakutenAuthUserInfo) {
                
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

#### claimMissionItem
```java
RakutenRewardJava.claimMissionItem(missionAchievementData, new CustomClaimCallback() {
    @Override
    public void success(@NonNull MissionAchievementData missionData) {
        
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }    
});
```

---
LANGUAGE :
> [![ja](../lang/ja.png)](../ja/java/README.md)
