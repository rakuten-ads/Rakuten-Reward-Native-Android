[TOP](../../README.md#top)　>　FAQ

Table of Contents
* [General](#general)
    * [Reward SDK is written in JAVA or Kotlin? My applcation is written in JAVA fully, is there any problem using the Reward SDK?](#reward-sdk-is-written-in-java-or-kotlin-my-applcation-is-written-in-java-fully-is-there-any-problem-using-the-reward-sdk)
    * [Can we access the staging environment for development / testing?](#can-we-access-the-staging-environment-for-development--testing)
* [Login Related](#login-related)
    * [What is Rakuten Auth login for?](#what-is-rakuten-auth-login-for)
    * [I'm using RID / RAE login option, do I have to call RakutenAuth.logout API when user logged out?](#im-using-rid--rae-login-option-do-i-have-to-call-rakutenauthlogout-api-when-user-logged-out)
    * [Can RakutenAuth.openLoginPage API be call in Fragment class?](#can-rakutenauthopenloginpage-api-be-call-in-fragment-class)
* [Implementation Related](#implementation-related)
    * [The API always return SDKNOTACTIVE error. What could be the cause?](#the-api-always-return-sdknotactive-error-what-could-be-the-cause)
    * [I have a daily launch app mission. How should I implement it?](#i-have-a-daily-launch-app-mission-how-should-i-implement-it)
    * [How can I implement the custom notification UI?](#how-can-i-implement-the-custom-notification-ui)
    * [How do I claim mission after a mission is achieved?](#how-do-i-claim-mission-after-a-mission-is-achieved)
    * [How do I implement onSDKStatusChanged or onUnclaimedAchievement?](#how-do-i-implement-onsdkstatuschanged-or-onunclaimedachievement)
    * [Is it possible to detect SDK Portal closed event?](#is-it-possible-to-detect-sdk-portal-closed-event)

---
# FAQ

## 全般的 
---
### Reward SDKはJAVAかKotlinで書かれたですか？私のアプリはJAVAで書かれたが、Reward SDKを使うなら何か問題がありますか？
<details>
    <summary>回答</summary>
Reward SDKはKotlinで書かれた。

Reward SDKはJAVAでもサポートできますが、APIを呼ぶにはすこし違うところがあります。

詳しいことは[ここ](../java/README.md)に参考してください。

</details>

<br>

### 開発/テストのために、ステージング環境にはアクセスできますか？
<details>
    <summary>回答</summary>
現在、開発/テストのために、ステージング環境は提供しておりません。
開発モードかもしくはテスト用のアカウントをご利用ください。

</details>

<br>

## ログイン関連
---
### Rakuten Auth loginとはなんですか？
<details>
    <summary>回答</summary>
RakutenAuth login オプションは楽天のログインをアプリで持っていらっしゃらないアプリケーション向けに提供しております(楽天のアプリケーションでログイン関連のSDKをご利用の場合はこちらを使用しなくても良いです)。

</details>

<br>

### 私はRID/RAEのログオンオプションを使っている、ユーザーがログアウト際に`RakutenAuth.logout` APIを呼ぶのは必要ですか？
<details>
    <summary>回答</summary>
Reward SDKバージョン<strong>３.１.１</strong>以上を使っている場合、どんなログインオプションを使うでも`RakutenAuth.logout` APIを呼ぶのは必要です。 

```kotlin
RakutenAuth.logout(object : LogoutResultCallback {
    override fun logoutSuccess() {
        //ログアウト成功
    }

    override fun logoutFailed(e: RakutenRewardAPIError) {
        //ログアウト失敗
    }
})
```

</details>

<br>

### `RakutenAuth.openLoginPage` API は `Fragment` クラスで呼ぶことができますか?
<details>
    <summary>回答</summary>
はい、できます。FragmentクラスでFragmentのインスタンスを提供して、Fragmentクラスの<code>onActivityResult</code> がトリガーされます。

Sample implementation
```kotlin
class TestLoginFragment : Fragment() {
    companion object {
        private const val LOGIN_REQ_CODE = 533
    }
     
    private fun login() {
        // requireActivity()じゃなくて、Fragmentのインスタンスを提供して
        RakutenAuth.openLoginPage(this, LOGIN_REQ_CODE)
    }
 
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == LOGIN_REQ_CODE) {
            if (resultCode == RESULT_OK) {
                RakutenAuth.handleActivityResult(data, object : LoginResultCallback {
                    override fun loginSuccess() {
                        // ログイン成功
                    }
 
                    override fun loginFailed(e: RakutenRewardAPIError) {
                        Toast.makeText(requireContext(), "Login Failed", Toast.LENGTH_SHORT).show()
                    }
                })
            } else {
                Toast.makeText(requireContext(), "Login Cancelled", Toast.LENGTH_SHORT).show()
            }
        }
    }
}
```

</details>

<br>

## 開発関連
---
### APIはいつも`SDKNOTACTIVE`のエラーを返す。原因は何ですか？
<details>
    <summary>回答</summary>

このエラーはReward SDKがまだアクティブにしてない意味です。

まずはApplicationクラスで初期化APIを呼ぶのかチェックして、提供したApp Codeが正しいか確認してください。
``` kotlin
RakutenReward.init(<AppCode>)
```

次はAPIを呼ぶのActivityクラスで[ここ](../basic/README.md#楽天リワードSDKポータル)のオプションを使うのかとチェックしてください。

もし以上のセットアップが正しくしたら、APIを呼ぶ前にSDKのステータスが<code>ONLINE</code>に変えるまでに待ってください。 
```kotlin
override fun onSDKStatusChanged(status: RakutenRewardSDKStatus) {
    if (status == RakutenRewardSDKStatus.ONLINE) {
        // SDKはもうアクティブになった、ここでAPIを呼ぶ
    }
}
```
</details>

<br>

### I have a daily launch app mission. How should I implement it?
<details>
    <summary>Answer</summary>

To log the mission's action code everytime user launch the app, you should wait the SDK status changed to <code>ONLINE</code> first. This is due to Reward SDK require some time to sync up data. 

The status changed will be triggered in the method below.
```kotlin
override fun onSDKStatusChanged(status: RakutenRewardSDKStatus) {
    if (status == RakutenRewardSDKStatus.ONLINE) {
        RakutenReward.logAction(<ActionCode>, {
            // log action success
        }) {
            // log action failed
        }
    }
}
```
</details>

<br>

### カステムでミッションのノーティフィケーションを作りたい
<details>
    <summary>回答</summary>
例えば、 Mission A は 3 回のアクションを必要とします。

```kotlin
RakutenReward.logAction(<ActionCode>, {
    // ログアクション成功
}) {
    // ログアクション失敗
}
```
logAction API が3回呼ばれると Mission A は達成します。そして、<code>RakutenRewardListener</code>の<code>onUnclaimedAchievement</code>がトリガーされます。

カスタムノーティフィケーションを表示する例
```kotlin
override fun onUnclaimedAchievement(achievement: MissionAchievementData) {
    if (achievement.custom // タイプを確認
        && RakutenRewardConfig.isUiEnabled() // ユーザのUI設定を確認
    ) {
        // UIを Main スレッドで表示する
    }
}
```

</details>

<br>

### How do I claim mission after a mission is achieved?
<details>
    <summary>Answer</summary>
Claim API is available in the <code>MissionAchievementData</code> object. 

```kotlin
achievement.claim({
    // claim success
}) {
    // claim failed
}
```

There are 2 ways to get <code>MissionAchievementData</code> object. 

First is when user achieved a CUSTOM notification type mission, <code>onUnclaimedAchievement</code> will be triggered.

```kotlin
override fun onUnclaimedAchievement(achievement: MissionAchievementData) {
    if (achievement.custom // check is notification type CUSTOM
        && RakutenRewardConfig.isUiEnabled() // check if user enable the UI setting
    ) {
        // Show custom UI in MAIN thread and call the following to claim mission
        achievement.claim({
            // claim success
        }) {
            // claim failed
        }
    }
}
```

Second is by calling get unclaim items API.

```kotlin
RakutenReward.getUnclaimedItems({ unclaimList ->
    unclaimList[0].claim({
        // claim success
    }) {
        // claim failed
    }
}) {
    // get unclaim items failed
}
```

</details>

<br>

### How do I implement `onSDKStatusChanged` or `onUnclaimedAchievement`?
<details>
    <summary>Answer</summary>
onSDKStatusChanged, onUnclaimAchievement are methods in RakutenRewardListener. Create a new object of RakutenRewardListener and provide your implementation for each methods.

```kotlin
val listener = object : RakutenRewardListener {
    override fun onUnclaimedAchievement(achievement: MissionAchievementData) {
        // user achieved a mission. This is mainly used for CUSTOM notification type.
    }
 
    override fun onUserUpdated(user: RakutenRewardUser) {
        // user data is updated
    }
 
    override fun onSDKStatusChanged(status: RakutenRewardSDKStatus) {
        // Reward SDK status changed
    }
 
    override fun onSDKClaimClosed(
        missionAchievementData: MissionAchievementData,
        status: RakutenRewardClaimStatus
    ) {
        // claim view is closed
    }
}
```
Then call the following APIs to add or remove the listener object. Remove listener API is required to prevent memory leak.

```kotlin
override fun onResume() {
    RakutenReward.addRakutenRewardListener(listener)
    super.onResume()
}
 
override fun onPause() {
    super.onPause()
    RakutenReward.removeRakutenRewardListener(listener)
}
```
> :grey_exclamation:  **If you are using `RakutenRewardBaseActivity` to start the SDK, the above are not needed as `RakutenRewardBaseActivity` class already handled it. You can simply override the method which you needed and provide you own implementation**

</details>

<br>

### Is it possible to detect SDK Portal closed event?
<details>
    <summary>Answer</summary>
Yes, it is possible to detect SDK portal closed event. Provide a unique request code to <code>openSDKPortal</code> API and <code>onActivityResult</code> will be triggered when SDK portal is closed.

Sample implementation

```kotlin
class SampleActivity : RakutenRewardBaseActivity() {
    companion object {
        private const val UNIQUE_REQ_CODE = 478
    }
 
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        RakutenReward.openSDKPortal(UNIQUE_REQ_CODE)
    }
 
    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if (requestCode == UNIQUE_REQ_CODE) {
            // handle SDK portal closed event
        } else {
            super.onActivityResult(requestCode, resultCode, data)
        }
    }
}
```
> :grey_exclamation:  **`RakutenReward.openSDKPortal()` API can be call in `Fragment` class as well, however `onActivityResult` will be triggered in Fragment class's parent activity instead**

</details>