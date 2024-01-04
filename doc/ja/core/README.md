[TOP](../README.md#top)　> コア API  

コンテンツ    
* [RakutenReward](#rakutenauth)  
* [RakutenRewardCoroutine](#rakutenrewardcoroutine)  
* [RakutenAuth](#rakutenauth)  
* [RakutenRewardConfig](#rakutenrewardconfig)  

---  

# コア API  
## RakutenReward  
`RakutenReward` クラスはリワードSDKのメインの設定や機能を提供しています。  
利用可能なAPIは[ここ](./RakutenReward.md)に参考してください。   

<br>  

## RakutenRewardCoroutine  
[![support version](http://img.shields.io/badge/core-3.3.3+-green.svg?style=flat)](https://github.com/rakuten-ads/Rakuten-Reward-Native-Android/releases/tag/rel_20220826_v3_3_0)  
`RakutenRewardCoroutine` クラスは suspend 関数の API を提供しています。  

| API 名                                               | 説明                      |
|-----------------------------------------------------|-------------------------|
| [getMissions](./RakutenReward.md#ミッションリスト)          | ミッションリストを取得する           |
| [getPointHistory](./RakutenReward.md#ポイント履歴)        | 3ヶ月前までのポイント履歴を取得する      |
| [logAction](./RakutenReward.md#アクションを送信する)          | ミッションを達成するためにアクションを送信する |
| [getUnclaimedItems](./RakutenReward.md#未獲得ミッションリスト) | 未獲得ミッションリストを取得する        |
| [memberInfo](./RakutenReward.md#会員情報)               | 最新の会員情報を取得する            |  

こちらの API は [`RewardApiResult`](../apiData/README.md#rewardapiresult) を返す。`Success` か `Failed`。   

```kotlin
val result = RakutenRewardCoroutine.memberInfo()
when (result) {
    is Success -> {
        result.data // APIデータ
    }
    is Failed -> {
        result.error // エラーコード
    }
}
```  

<br>  

## RakutenAuth  
`RakutenAuth` クラスは楽天のログインに関するAPIを提供しております。  

| API 名                                                                        | 説明                  | 
|------------------------------------------------------------------------------|---------------------|
| [openLoginPage](../basic/LOGIN.md#1-show-login-page)                         | ログインページを開く          |
| [handleActivityResult](../basic/LOGIN.md#2-get-result-from-onactivityresult) | ログインの結果を処理          | 
| [hasUserSignedIn](../basic/UserInfo.md#check-if-user-is-signed-in)           | ログインしているかどうか状態を取得する |
| [logout](../basic/README.md#log-out)                                         | ログアウトする             | 
| [getUserName](../basic/UserInfo.md#get-users-full-name)                      | 楽天会員名を取得する          |
| [getUserInfo](../basic/UserInfo.md#get-users-current-point-and-rank)         | 楽天ランクとポイントを取得する     |  

<br>  

## RakutenRewardConfig
`RakutenRewardConfig` はユーザー設定を管理するクラスです。  

| API 名            | 説明                                                       | 
|------------------|----------------------------------------------------------|
| isOptedOut       | オプトアウトの状態を取得する <br><b>true</b> : オプトアウト (リワードSDKは動作しません) |
| setOptedOut      | オプトアウトの状態を設定する                                           | 
| isUiEnabled      | ミッションのUIのオン・オフ設定を取得する                                    | 
| setUiEnabled     | ミッションのUIのオン・オフを設定する                                      |
| isDebuggable     | SDKデバッグができるように設定する                                       | 
| isUsingSdkPortal | SDKポータルを使う、使わないを設定する (UIモジュールのみ)                         |  

<br>  

---
言語 :
> [![en](../../lang/en.png)](../../core/README.md)   
