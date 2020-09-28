[トップ](../README.md#top)　>基本ガイド

---
# SDKの初期化
楽天リワードSDKを利用するにははじめに初期化が必要です(SDKユーザーの基本データを取得します)
SDKの機能を利用するのにはRakutenRewardクラスのメソッドを利用します

```kotlin
RakutenReward.token = "<accesstoken>"
RakutenReward.appCode = "<AppCode>"  // Example anAuY28ucmFrdXRlbi5yZXdhcmQuYW5kcm9pZC1sRUdqNEhETS1pdXNZbWRLT2JVRGFLVV9fQ0ZLd2lacg==

```

| パラメータ名        | 説明           
| --- | --- 
| appCode | アプリケーションキー (楽天リワードSDKの開発者ポータルより取得) 
| token | API-C アクセストークン(楽天リワードSDK APIへの接続用) |
  
セッションは Activity onStart メソッドで開始されます  
SDKを初期化するにはいくつかの方法があります


### 1 RakutenRewardLightBaseActivity を拡張した Activity クラスを作る
```kotlin
class YourActivity : RakutenRewardBaseActivity {}
```

### 2 Android のライフサイクル上でメソッドをコールする
```kotlin
class YourActivity : Activity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        RakutenRewardLifecycle.onCreate(this)
    }

    override fun onStart() {
        super.onStart()
        RakutenRewardLifecycle.onStart(this)
    }

    override fun onDestroy() {
        super.onDestroy()
        RakutenRewardLifecycle.onDestroy()
    }
}
```


### 3 AndroidX ライフサイクルイベントをバインドする
```kotlin
class YourActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        RakutenRewardManager.bindRakutenRewardIn(this, this)
    }

}
```

この方法で行うためには Activity に LifecycleOwner を実装する必要があります

---
# ログイン

### 1. ログインページを表示する　`RakutenAuth.openLoginPage()`
```kotlin
RakutenAuth.openLoginPage(context, REQUEST_THIRD_PARTY_LOGIN)
```

![Login](Login.jpg)


### 2.  ログイン終了の結果を受け取る `onActivityResult()`
```kotlin
override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        if (requestCode == REQUEST_THIRD_PARTY_LOGIN) {
            if (resultCode == RESULT_OK) {
                handleActivityResult(data)
            } else {
                // ユーザーがログインをキャンセルした
            }
        }
    }
```

### 3. ログインの最終的なプロセスを受け取る `RakutenAuth.handleActivityResult()`
```kotlin
private fun handleActivityResult(data: Intent?) {
        RakutenAuth.handleActivityResult(data, object : LoginResultCallback {
            override fun loginSuccess() {
                //✅ ログイン成功
            }

            override fun loginFailed(e: RakutenRewardAPIError) {
                //⛔ ログイン失敗
            }
        })
    }
```

ログインの画面終了後、APIへのアクセスに必要なデータ処理を行います。楽天へのログインは2で終了しておりますが、　　  
データ処理をを受け取るにはこちらのようなコールバックを待っていただく必要があります

---
# ログアウト
`RakutenAuth.logout()`
```kotlin
private fun logout() {
    RakutenAuth.logout(object : LogoutResultCallback {
            override fun logoutSuccess() {
                //ログアウト 完了
            }

            override fun logoutFailed(e: RakutenRewardAPIError) {
                //ログアウト失敗
            }
        })
}
```

---
# ユーザー情報を取得する

こちらは楽天会員情報を取得するAPIになっております

## ユーザーがログインしているかどうか
```kotlin
RakutenAuth.hasUserSignedIn(): Boolean
```

## ユーザーの名前を取得する　
```kotlin
RakutenAuth.getUserName(context: Context): String
```

##  ユーザーの会員ランク楽天ポイントを取得する
```kotlin
RakutenAuth.getUserInfo(
    success = { userInfo ->
        // ポイント　
        userInfo.points
        
        // ランク
        userInfo.rank
    }, 
    failed = {
        // 取得に失敗
    }
)
```

---
# ミッションの達成
ミッションを達成するには、開発者はアクションAPIをコールします  
ミッション達成後、ミッション達成UIが表示されます

## アクションを送信する
```kotlin
RakutenReward.logAction("<actionCode>", {}, {})
```
actionCode は開発者ポータルより取得します

## ミッション達成UI
ユーザーがミッションを達成すると、下記のようなミッション達成UIが表示されます  
楽天リワードではモーダルとバナーを用意しております

![Modal](Modal.jpeg)     ![Banner](Banner.jpeg)

### ミッション達成UIの種類
楽天リワードSDKは4つの種類のミッション達成の種類があります  
モーダル、バナー、UIなし、カスタム  
これらの設定は開発者ポータルから設定できます

| ミッション達成UIの種類        | 説明
| --- | ---
| モーダル | モーダルUIを表示する
| バナー | バナーUIを表示する
| カスタム | 開発者が自由にUIを作成できます
| UIなし | UIを表示しません

## 楽天リワードSDKポータル
ユーザーにリワードサービスの情報(ミッションや進捗、ポイントなど)を伝えるために  
楽天リワードSDKではポータルというのを提供しております  
このポータルを表示するにはポータル表示のAPIを呼ぶ必要があります

こちらがSDKポータルのイメージになります

![Portal1](Portal1.png)

![Portal2](Portal2.png)

![Portal3](Portal3.png)

![Portal4](Portal4.png)

![Portal5](Portal5.png)

---
言語 :
> [![en](../../lang/en.png)](../../basic/README.md)
