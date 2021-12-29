[TOP](../README.md#top)　> Java アプリケーション開発者

コンテンツ
* [Javaアプリケーション開発者様)](#Javaアプリケーション開発者様)<br>
* [APIへのアクセス方法](#APIへのアクセス方法)<br>
* [プロパティーについて](#プロパティーについて)<br/>
* [Kotlinコールバック](#Kotlinコールバック)<br/>
* [Javaスタイルのコールバック](#Javaスタイルのコールバック)<br><br>

---
# Javaアプリケーション開発者様)
このSDKは100%Kotlinで作られています。<br/>
KotlinのObject、Extension、Companion Object を Java からアクセスするには
工夫が必要です。<br/>

## APIへのアクセス方法
### RakutenReward
RakutenReward クラスはKotlinのobjectです, このobjectにあるメソッドをコールするには、INSTANCE を呼び出す必要があります。
```java
RakutenReward.INSTANCE.init(this, "<Appcode>");
```
SDK 2.3.0 からは　INSTANCE を呼び出す必要はありません。
```java
RakutenReward.init(this, "<Appcode>");
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

### RakutenReward.openAdPortal()
こちらは uiモジュールのメソッドですが、 Kotlin の Extension を使用しています。<br/>
こちらは以下のように呼び出す必要があります。<br/>

```java
RakutenRewardExtensionKt.openAdPortal(RakutenReward.INSTANCE, <activity context>);
RakutenRewardExtensionKt.openAdPortal(RakutenReward.INSTANCE, <activity context>, <request code>);
```

## プロパティーについて

Kotlin はプロパティーに直接アクセスできますが、Javaでは　getXxx というスタイルで呼び出す必要があります<br/>

```java
String version = RakutenReward.INSTANCE.getVersion();
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
上記のKotlinスタイルのコールバックを利用しない方法もご用意しています。<br/>

### RakutenReward
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


#### getMissionsJava (Kotioln: getMissions)
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
言語 :
> [![en](../../lang/en.png)](../../java/README.md)