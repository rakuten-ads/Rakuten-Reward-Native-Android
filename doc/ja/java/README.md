[TOP](../README.md#top)　> Java アプリケーション開発者

コンテンツ
* [Javaアプリケーション開発者様)](#javaアプリケーション開発者様)<br>
* [Mission-Javaモジュール](#Mission-Javaモジュール)<br>
* [APIへのアクセス方法](#APIへのアクセス方法)<br>
* [プロパティーについて](#プロパティーについて)<br/>
* [Kotlinコールバック](#Kotlinコールバック)<br/>
* [Javaスタイルのコールバック](#Javaスタイルのコールバック)<br><br>

---
# Javaアプリケーション開発者様)
このSDKは100%Kotlinで作られています。<br/>
Java開発者様向けに、Java対応のAPIを提供するmission-javaモジュールを用意しています。<br/>

## Mission-Javaモジュール
Javaプロジェクトでは、Java向けのクリーンなAPIを提供する**mission-java**モジュールの使用を推奨します。Kotlinの知識が不要です。

### 依存関係
アプリのbuild.gradleにmission-javaの依存関係を追加してください：
```gradle
implementation 'com.rakuten.gap:rewardsdknative-java'
```

### インポート
```java
import com.rakuten.gap.ads.mission_java.RakutenRewardJava;
import com.rakuten.gap.ads.mission_java.listeners.*;
```

## APIへのアクセス方法
### RakutenReward
RakutenReward クラスはKotlinのobjectです, このobjectにあるメソッドをコールするには、INSTANCE を呼び出す必要があります。
```java
RakutenReward.INSTANCE.init("<Appcode>");
```
SDK 2.3.0 からは　INSTANCE を呼び出す必要はありません。
```java
RakutenReward.init("<Appcode>");
```

### RakutenReward.openSDKPortal()
こちらは uiモジュールのメソッドですが、 Kotlin の Extension を使用しています。<br/>
こちらは以下のように呼び出す必要があります。<br/>

```java
RakutenRewardExtensionKt.openSDKPortal(RakutenReward.INSTANCE);
```
SDK 2.4.0 から
```java
boolean success = RakutenRewardExtensionKt.openSDKPortal(RakutenReward.INSTANCE);
boolean success = RakutenRewardExtensionKt.openSDKPortal(RakutenReward.INSTANCE, <requestCcode>);
```

## プロパティーについて

Kotlin はプロパティーに直接アクセスできますが、Javaでは　getXxx と setXxx というスタイルで呼び出す必要があります<br/>

```java
String version = RakutenReward.INSTANCE.getVersion();

RakutenReward.INSTANCE.setTokenType(RakutenRewardTokentype.RID);
```

## Kotlinコールバック
このSDKでは、メソッドのコールバックにラムダ式を使っています。</br>
その中に、Kotlin の Unit (Javaだと voidに当たる) は、Kotlinのスタンダードライブラリに
含まれており、こちらを Javaから使用するには、Kotlin を入れる必要があります。<br/>
詳細は、Android の公式ドキュメント(Add Kotlin to an existing app)[https://developer.android.com/kotlin/add-kotlin] をご参照ください。<br/>

```java
RakutenReward.INSTANCE.logAction("", () -> { return Unit.INSTANCE; }, (RakutenRewardAPIError e) -> { return Unit.INSTANCE; });
```

## Javaスタイルのコールバック
mission-javaモジュールを通じてJava向けのコールバックAPIを提供しています。<br/>

### RakutenRewardJava
RakutenRewardJavaクラスは「Java」サフィックスを付けないクリーンなJava APIを提供します。<br/>
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
// コールバックありの場合
RakutenRewardJava.requestForConsent(new RequestForConsentCallback() {
    @Override
    public void onRequestConsentResult(@NonNull RakutenRewardConsentStatus status) {

    }
});

// コールバックなしの場合
RakutenRewardJava.requestForConsent();
```

#### showConsentBanner
```java
// コールバックありの場合
RakutenRewardJava.showConsentBanner(new RequestForConsentCallback() {
    @Override
    public void onRequestConsentResult(@NonNull RakutenRewardConsentStatus status) {

    }
});

// コールバックなしの場合
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
言語 :
> [![en](../../lang/en.png)](../../java/README.md)