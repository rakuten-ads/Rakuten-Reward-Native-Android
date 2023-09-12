[TOP](../README.md#top)　>　Special Guide

---
# ログインオプション
## ログイン方法の変更
リワードSDK では3種類のログイン方法を提供しております。  
ご利用の環境に合わせて、適切なものをご利用ください。  
初期設定では、RAKUTEN_AUTH　になっております。

| ログインオプション    | 説明                                               | サポートしているリージョン |
|--------------|--------------------------------------------------|---------------|
| RAKUTEN_AUTH | 初期設定、ログインやユーザーの処理を全てリワードSDKが担当します                | Japan, Taiwan |
| RID          | ログイン部分はID SDKが担当します（RID)。トークンをリワードSDKに渡す必要があります  | Japan         |  
| RAE          | ログイン部分はID SDKが担当します(RAE)。 トークンをリワードSDKに渡す必要があります | Japan         |

### ログインオプションを切り替える

初期設定では、リワードSDKが用意したログインになります。(RAKUTEN_AUTH)

### RAKUTEN_AUTH
```kotlin
RakutenReward.tokenType = RakutenRewardTokentype.RAKUTEN_AUTH
```

### RID
```kotlin
RakutenReward.tokenType = RakutenRewardTokentype.RID
```
リワードSDKのAPIを利用するには、トークンの設定が必要です  
```kotlin
RakutenReward.setRIdToken("token")
```

ログインの実装方法についてはID　SDK の詳細をご参照ください。

### RAE
```kotlin
RakutenReward.tokenType = RakutenRewardTokentype.RAE
```

リワードSDKのAPIを利用するには、トークンの設定が必要です  
```kotlin
RakutenReward.setRaeToken("token")
```

ログインの実装方法についてはID　SDK の詳細をご参照ください。

---
言語 :
> [![en](../../lang/en.png)](../../special/README.md)