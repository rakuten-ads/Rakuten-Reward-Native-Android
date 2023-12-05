[TOP](/README.md#top)　>　[Basic Guide](./README.md)　>　User Information  

---  

# User Information
List of available API to retrieve user information  
> These API are eligible for `RAKUTEN_AUTH` login options only.  

## Check if user is signed in
```kotlin
RakutenAuth.hasUserSignedIn()
```  

## Get user's full name  
```kotlin
RakutenAuth.getUserName(): String
```  

## Get user's current point and rank  
```kotlin
RakutenAuth.getUserInfo(
    success = { userInfo ->
        //get point
        userInfo.points
        
        //get rank
        userInfo.rank
    }, 
    failed = {
        //fail to get user info
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
| Property name | Description                      |
|---------------|----------------------------------|
| points        | Total Rakuten point for the user |
| rank          | User's Rakuten account rank      |
  
#### Rakuten Account Rank  
| Rank | Description |
|------|-------------|
| 1    | Regular     |
| 2    | Silver      |
| 3    | Gold        |
| 4    | Platinum    |
| 5    | Diamond     |  

<br>  

---
LANGUAGE :
> [![ja](../lang/ja.png)](../ja/basic/UserInfo.md)