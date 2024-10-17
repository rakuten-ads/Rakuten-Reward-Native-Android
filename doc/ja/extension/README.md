[TOP](../../README.md#top) > 拡張機能    

# JavaScript 拡張機能    
ネイティブアプリケーションでは、ページがWebベースでネイティブのWebViewに表示されるページがいくつかあります。  
このライブラリは、WebページからSDK APIをトリガーするユースケースのために作成されました。 

# SDKの設定  
このガイドはAndroidの実装ガイドです。JavaScriptの実装ガイドについては、[こちら](https://github.com/rakuten-ads/Rakuten-Reward-JS/tree/main/js-extension-library/ja)を参照してください。

## SDK のインポート  
SDKをインポートするために、モジュールのbuild.gradleに以下を追加します。  

```groovy
    // Import the BoM for the Reward Native platform
    implementation platform('com.rakuten.android:rewardsdknative-bom:x.x.x')
    // ... other library
    implementation 'com.rakuten.android:rewardsdknative-ext'
```  

## 初期化  
この機能を初期化するために、以下のAPIを呼び出します。  

```kotlin  
RewardJS.setupWebView("<appCode>", "<domain>", webView)
```  
| パラメータ | 説明 |
| --- | --- |
| appCode | アプリケーションキー (こちらは楽天リワードの開発者ポータルから取得できます) |
| domain | `missionsdk-ext` が実装されているWebページのドメイン |
| webView | Webページを読み込むWebViewインスタンス |  

## サポートされているAPI
現在、この拡張ライブラリは以下のAPIをサポートしています:
* `RakutenReward.logAction`
* `RakutenReward.openSDKPortal`  
* `RakutenReward.openSpsPortal`

APIが正常に動作するためには、ActivityまたはWebViewページがFragment内にある場合、親ActivityでSDKセッションを開始する必要があります。   
[こちらを参照](../basic/README.md#activity-と紐づけてsdk機能をアクティブにする)

---
言語 :
> [![en](../../lang/en.png)](../../extension/README.md) 
