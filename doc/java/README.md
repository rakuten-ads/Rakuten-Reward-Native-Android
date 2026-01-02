[TOP](../../README.md#top)　> Java App Developers

Table of Contents
* [For Java Developers](#for-java-developers)<br>
* [How to access API](#how-to-access-api)<br>
* [Properties](#properties)<br/>
* [Callback Kotlin](#callback-kotlin)<br/>
* [Callback Java Style](#callback-java-style)<br><br>

---
# For Java Developers
This SDK is written by Kotlin.<br/>
So, to access Kotlin Object, Extension, Companion Object,
need some techniques.<br/>

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
We prepared Java friendly callback style for APIs.<br/>

### RakutenReward
We prepared same function without Kotlin callback.<br/>
#### loginActionJava(Kotlin : loginAction)
```java
RakutenReward.logActionJava("", new LogActionCallback() {
    @Override
    public void success() {
        
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

#### memberInfoJava (Kotlin : memberInfo)
```java
RakutenReward.memberInfoJava(new MemberInfoCallback() {
    @Override
    public void success(@NonNull RakutenRewardUser rakutenRewardUser) {
        
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```


#### getMissionsJava (Kotlin: getMissions)
```java
RakutenReward.getMissionsJava(new GetMissionsCallback() {
    @Override
    public void success(@NonNull List<MissionData> list) {
        
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

#### getUnclaimedItemsJava (Kotlin: getUnclaimedItems)
```java
RakutenReward.getUnclaimedItemsJava(new UnclaimedItemCallback() {
    @Override
    public void success(@NonNull List<MissionAchievementData> list) {
        
    }

    @Override
    public void failed(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

#### getPointHistoryJava (Kotlin: getPointHistory)
```java
RakutenReward.getPointHistoryJava(new PointHistoryCallback() {
    @Override
    public void success(@NonNull RakutenRewardPointHistory rakutenRewardPointHistory) {

    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

### RakutenAuth
#### getUserInfoJava (getUserInfo)
```java
RakutenAuth.getUserInfoJava(new AuthMemberInfoCallback() {
    @Override
    public void success(@NonNull RakutenAuthUserInfo rakutenAuthUserInfo) {
                
    }

    @Override
    public void fail(@NonNull RakutenRewardAPIError rakutenRewardAPIError) {

    }
});
```

### MissionAchievementData
#### claimJava()
```java
missionAchievementData.claimJava(new CustomClaimCallback() {
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
