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

APIが正常に動作するためには、ActivityまたはWebViewページがFragment内にある場合、親ActivityでSDKセッションを開始する必要があります。   
[こちらを参照](../basic/README.md#activity-と紐づけてsdk機能をアクティブにする)

---

## 同意処理について（2.1.1以降）

2.1.1以降、ユーザーがまだ楽天リワードの利用規約に同意していない場合、APIを呼び出すと自動的に同意ダイアログが表示されます。APIはユーザーが同意した場合のみ実行されます。ユーザーが拒否した場合、APIの呼び出しは実行されません。

---

## サポートされているAPI

| API | 説明 |
| --- | --- |
| `logAction(appKey, actionCode)` | ミッションアクションを記録する |
| `logAction(appKey, actionCode, callback)` | 結果コールバック付きでミッションアクションを記録する |
| `openSdkPortal(appKey)` | リワードSDKポータルを開く |
| `openSdkPortal(appKey, callback)` | 結果コールバック付きでリワードSDKポータルを開く |
| `openSpsPortal(appKey)` | SPSポータルを開く |
| `openSpsPortal(appKey, callback)` | 結果コールバック付きでSPSポータルを開く |
| `getUserRewardPoint(appKey, callback)` | ユーザーの現在のリワードポイント残高を取得する |
| `getPointHistory(appKey, callback)` | ユーザーのポイント履歴を取得する |
| `getMissionLite(appKey, callback)` | ミッションリストを取得する（ライト版・進捗なし） |
| `getMissionDetails(appKey, actionCode, callback)` | 進捗を含む単一ミッションの詳細を取得する |
| `getUnclaimList(appKey, callback)` | 未クレームのミッション達成リストを取得する |
| `claimMissionPoint(appKey, actionCode, achievedDate, callback)` | ミッション達成のポイントをクレームする |

---

## バージョンマッピング

| BOM   | JS |
|-------| --- |
| 8.2.1 | 1.3.0 |
| 7.6.0 | 1.2.0 |
| 7.5.0 | 1.1.0 |
| 6.2.0 | 1.0.0 |

---

言語 :
> [![en](../../lang/en.png)](../../extension/README.md) 
