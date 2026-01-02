# V8 マイグレーションガイド

## 概要
このガイドでは、従来のAPIパターンからSDK v8で導入されたRewardTokenProviderアプローチへの移行方法を説明します。

> **注意:** 従来の`setRIdToken()`および`setRaeToken()` APIは非推奨ですが、引き続きサポートされています。ただし、v8の自動トークン有効期限処理の恩恵は受けられません。より良いエクスペリエンスのため、`RewardTokenProvider`への移行を推奨します。

## トークン管理の変更

### 旧方式（非推奨）
以前は、SDK利用前にアクセストークンを直接設定する必要がありました：

```kotlin
// 旧方式 - 非推奨ですが引き続き動作します
RakutenReward.setRIdToken(accessToken)
// または
RakutenReward.setRaeToken(accessToken)
```

**注意:** これらのAPIは引き続き機能しますが、トークン有効期限（TOKENEXPIREエラー）の手動処理が必要です。自動トークン管理の恩恵を受けるには`RewardTokenProvider`への移行が必要です。

### 新方式（v8以降）
SDK初期化時にRewardTokenProviderインスタンスを渡す必要があります：

```kotlin
// 新方式 - RewardTokenProviderを利用
val tokenProvider = object: RewardTokenProvider {
    override suspend fun getAccessToken(): String {
        // ここでアクセストークンを返却
        return "token"
    }
}

RakutenReward.init(tokenProvider)
```

## 新方式のメリット

1. **トークン管理の向上**: プロバイダーパターンにより、SDKの再初期化なしで動的にトークンを更新可能
2. **トークン有効期限の自動処理**: `TOKENEXPIRED`エラーコードの個別対応が不要
3. **ステータス管理の簡素化**: `ONLINE`ステータス待機が不要

## 移行手順

### ステップ1: 非推奨APIの削除
以下のAPI呼び出しを削除してください：

```kotlin
// 削除対象
RakutenReward.setRIdToken(token)
RakutenReward.setRaeToken(token)
RakutenReward.startSession() // 不要 - SDKが自動的にセッションを管理
```

**注意:** 以前は、トークン提供後に`startSession()`を呼び出してSDKセッションを手動で開始する必要がありました。`RewardTokenProvider`を使用すると、SDKが自動的にセッションを管理します。

### ステップ2: RewardTokenProviderの実装
`RewardTokenProvider`インターフェースを実装したトークンプロバイダーを作成します：

```kotlin
val tokenProvider = object: RewardTokenProvider {
    override suspend fun getAccessToken(): String {
        // 認証システムからトークンを返却
        return if (isUserLoggedIn()) {
            // ユーザーがログインしている場合は有効なアクセストークンを返却
            yourAuthManager.getAccessToken()
        } else {
            // ユーザーがログインしていない場合は空文字列を返却
            ""
        }
    }
}
```

**重要**:
- ユーザーがログインしている場合: 認証システムから有効かつ期限切れでないアクセストークンを返却してください
- ユーザーがログインしていない場合: 空文字列（`""`）を返却してください
- SDKは必要なタイミングでこのメソッドを呼び出します

### ステップ3: SDK初期化時にトークンプロバイダーを渡す
アプリ初期化時に`RakutenReward.init()`へトークンプロバイダーを渡します：

```kotlin
class App: Application() {
    override fun onCreate() {
        super.onCreate()
        // トークンプロバイダーでSDK初期化
        RakutenReward.init(tokenProvider)
    }
}
```

### ステップ4: トークン有効期限処理の削除
従来は`TOKENEXPIRED`ステータスの個別処理が必要でしたが、v8以降は不要です：

```kotlin
override fun onSDKStatusChanged(status: RakutenRewardSDKStatus) {
    when (status) {
        // 削除 - 不要
        RakutenRewardSDKStatus.TOKENEXPIRED -> {
            // トークン有効期限処理は削除
        }
    }
}
```

SDKは必要に応じて`getAccessToken()`を自動で呼び出します。

### ステップ5: ONLINEステータスチェックの削除
従来は`ONLINE`ステータスを待ってからSDK機能を利用していましたが、v8以降は不要です：

```kotlin
// 旧方式 - 削除対象

// パターン1: API呼び出し前のステータスチェック
if (RakutenReward.status == RakutenRewardSDKStatus.ONLINE) {
    RakutenReward.logAction(code) // この条件分岐は削除
}

// パターン2: コールバックでONLINE待機
override fun onSDKStatusChanged(status: RakutenRewardSDKStatus) {
    when (status) {
        RakutenRewardSDKStatus.ONLINE -> {
            RakutenReward.logAction(code) // この実行も削除
        }
    }
}
```

```kotlin
// 新方式 - 直接API利用
RakutenReward.logAction(code) // tokenProviderで初期化後は直接呼び出し可能
```

## MemberInfo API呼び出しタイミングの変更

### 背景
以前のSDKバージョンでは、SDKセッション開始方法（RakutenRewardBaseActivity、RakutenRewardLifecycle、RakutenRewardManager）に関わらず、SDKは`onStart()`ライフサイクルで`memberInfo` APIを呼び出していました。これにより、ユーザーがアクティビティに戻るたび（バックグラウンドから、または他の画面から）に最新のユーザーデータが保証されましたが、バックエンドへのトラフィックが高くなっていました。

### v8での変更点
SDKは`onCreate()`でのみ`memberInfo` APIを呼び出すようになり、バックエンドAPIコールが大幅に削減されました。この変更は以下のすべてのSDKセッション開始方法に影響します：
- `RakutenRewardBaseActivity`
- `RakutenRewardLifecycle.onStart()`
- `RakutenRewardManager.bindRakutenRewardIn()`

**影響:**
- ✅ バックエンドAPIコールの削減
- ⚠️ アクティビティ復帰時にユーザーデータが自動更新されない
- ⚠️ アクティビティ再開時に`ONLINE`ステータス変更コールバックが発生しない

### 手動でユーザーデータを更新する必要がある場合

**手動更新が不要な場合:**
- アプリでユーザーデータ（ポイント、未獲得数）を表示していない
- SDK APIの呼び出しのみ必要（logAction、getMissionsなど） - 手動更新なしで動作します

**手動更新が必要な場合:**
- UIでユーザーポイント（`user.point`）または未獲得数（`user.unclaimed`）を表示している
- ユーザーが画面に戻った際に最新のユーザーデータを確保する必要がある

### ユーザーデータを手動で更新する方法

最新データが必要な場合は`memberInfo` APIを呼び出してください。これはすべてのSDKセッション開始方法に適用されます：

**コールバック版:**
```kotlin
override fun onStart() {
    super.onStart()

    // 必要に応じてユーザーデータを手動で更新
    RakutenReward.memberInfo({ user ->
        // 最新のユーザーデータでUIを更新
        updateUI(user.point, user.unclaimed)
    }, { error ->
        // エラー処理
    })
}
```

**コルーチン版:**
```kotlin
override fun onStart() {
    super.onStart()

    lifecycleScope.launch {
        when (val result = RakutenRewardCoroutine.memberInfo()) {
            is Success -> {
                val user = result.data
                updateUI(user.point, user.unclaimed)
            }
            is Failed -> handleError(result.error)
        }
    }
}
```

## エラー処理

v8ではエラー処理が簡素化されています：

- **トークン有効期限**: SDKが自動で処理（`RewardTokenProvider`使用時）
- **無効なトークン**: SDKがプロバイダー経由で新しいトークンを要求

アプリ固有のビジネスロジックエラーのみ個別に対応してください。

---
言語 :
> [![en](../../lang/en.png)](../../migration/v8-migration.md)