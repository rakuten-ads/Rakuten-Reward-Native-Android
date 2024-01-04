[トップ](../README.md#top)　>　[基本ガイド](./README.md)　>　ユーザー情報 

---  

# ユーザー情報
こちらは楽天会員情報を取得するAPIになっております  
> こちらのAPIは `RAKUTEN_AUTH` のみ使える  

## ユーザーがログインしているかどうか
```kotlin
RakutenAuth.hasUserSignedIn()
```  

## ユーザーの名前を取得する  
```kotlin
RakutenAuth.getUserName(): String
```  

## ユーザーの会員ランク楽天ポイントを取得する  
```kotlin
RakutenAuth.getUserInfo(
    success = { userInfo ->
        //ポイント
        userInfo.points
        
        //ランク
        userInfo.rank
    }, 
    failed = {
        //取得に失敗
    }
)
```  
<details>
    <summary>JAVA</summary>

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
</details>  

### RakutenAuthUserInfo  
| 名前     | 説明           |
|--------|--------------|
| points | ユーザの楽天ポイント   |
| rank   | ユーザーの楽天会員ランク |
  
#### 楽天会員ランク  
| ランク | 説明     |
|-----|--------|
| 1   | レギュラー  |
| 2   | シルバー   |
| 3   | ゴールド   |
| 4   | プラチナ   |
| 5   | ダイヤモンド |  

<br>  

---
言語 :
> [![en](../../lang/en.png)](../../basic/UserInfo.md)