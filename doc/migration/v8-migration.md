# V8 Migration Guide

## Overview
This guide explains how to migrate from the old API pattern to the new RewardTokenProvider approach introduced in SDK v8.

> **Note:** The old `setRIdToken()` and `setRaeToken()` APIs are deprecated but still supported. However, they do not benefit from v8's automatic token expiry handling. We recommend migrating to `RewardTokenProvider` for a better experience.

## Token Management Changes

### Old Way (Deprecated)
Previously, SDK consumers needed to provide an access token before using the SDK:

```kotlin
// Old approach - deprecated but still works
RakutenReward.setRIdToken(accessToken)
// or
RakutenReward.setRaeToken(accessToken)
```

**Note:** These APIs still function but require manual handling of token expiry (TOKENEXPIRE errors). Migrate to `RewardTokenProvider` to benefit from automatic token management.

### New Way (v8+)
Now, consumers should provide a RewardTokenProvider instance during SDK initialization:

```kotlin
// New approach - using RewardTokenProvider
val tokenProvider = object: RewardTokenProvider {
    override suspend fun getAccessToken(): String {
        // return the access token here
        return "token"
    }
}

RakutenReward.init(tokenProvider)
```

## Benefits of the New Approach

1. **Better Token Management**: The token provider pattern allows for dynamic token updates without reinitializing the SDK
2. **Automatic Token Expiry Handling**: The SDK now handles token expiry cases internally - you no longer need to handle `TOKENEXPIRED` error codes
3. **Simplified Status Management**: No need to wait for `ONLINE` status before using SDK features


## Migration Steps

### Step 1: Remove Deprecated API Calls
Remove the following API calls from your code:

```kotlin
// Remove these deprecated calls
RakutenReward.setRIdToken(token)
RakutenReward.setRaeToken(token)
RakutenReward.startSession() // No longer needed - SDK handles session automatically
```

**Note:** Previously, you needed to call `startSession()` after providing a token to manually start the SDK session. With `RewardTokenProvider`, the SDK automatically manages the session for you.

### Step 2: Implement RewardTokenProvider
Create a token provider that implements the `RewardTokenProvider` interface:

```kotlin
val tokenProvider = object: RewardTokenProvider {
    override suspend fun getAccessToken(): String {
        // Return token from your authentication system
        return if (isUserLoggedIn()) {
            // Return valid access token when user is logged in
            yourAuthManager.getAccessToken()
        } else {
            // Return empty string when user is not logged in
            ""
        }
    }
}
```

**Important**:
- When user is logged in: Return a valid, non-expired access token from your authentication system
- When user is NOT logged in: Return an empty string (`""`)
- The SDK will call this method whenever it needs a token

### Step 3: Initialize SDK with Token Provider
Pass the token provider to `RakutenReward.init()` during app initialization:

```kotlin
class App: Application() {
    override fun onCreate() {
        super.onCreate()
        // Initialize SDK with token provider
        RakutenReward.init(tokenProvider)
    }
}
```

### Step 4: Remove Token Expiry Handling
In previous SDK versions, you needed to handle `TOKENEXPIRED` status manually. This is no longer required:

```kotlin
override fun onSDKStatusChanged(status: RakutenRewardSDKStatus) {
    when (status) {
        // Remove this - no longer needed
        RakutenRewardSDKStatus.TOKENEXPIRED -> {
            // Token expiry handling code can be removed
        }
    }
}
```

The SDK now handles token expiry automatically by calling your `getAccessToken()` method when needed.

### Step 5: Remove ONLINE Status Checks
Previously, you had to wait for `ONLINE` status before using SDK features. This is no longer required:

```kotlin
// OLD WAY - Remove these patterns:

// Pattern 1: Status check before API calls
if (RakutenReward.status == RakutenRewardSDKStatus.ONLINE) {
    RakutenReward.logAction(code) // Remove this conditional check
}

// Pattern 2: Waiting for ONLINE status in callback
override fun onSDKStatusChanged(status: RakutenRewardSDKStatus) {
    when (status) {
        RakutenRewardSDKStatus.ONLINE -> {
            RakutenReward.logAction(code) // Remove this conditional execution
        }
    }
}
```

```kotlin
// NEW WAY - Direct API usage:
RakutenReward.logAction(code) // Call directly after init with token provider
```

## MemberInfo API Timing Change

### Background
In previous SDK versions, regardless of which method you used to start the SDK session (RakutenRewardBaseActivity, RakutenRewardLifecycle, or RakutenRewardManager), the SDK called `memberInfo` API in the `onStart()` lifecycle. This ensured fresh user data whenever the user returned to the activity (from background or another screen), but caused high backend traffic.

### What Changed in v8
The SDK now calls `memberInfo` API in `onCreate()` only, significantly reducing backend traffic. This affects all SDK session start methods:
- `RakutenRewardBaseActivity`
- `RakutenRewardLifecycle.onStart()`
- `RakutenRewardManager.bindRakutenRewardIn()`

**Impact:**
- ✅ Reduced backend API calls
- ⚠️ User data is not automatically refreshed when returning to an activity
- ⚠️ No `ONLINE` status change callback when resuming activities

### When to Manually Refresh User Data

**You DON'T need to manually refresh if:**
- Your app doesn't display user data (points, unclaimed count)
- You only need to call SDK APIs (logAction, getMissions, etc.) - these work without manual refresh

**You NEED to manually refresh if:**
- You display user points (`user.point`) or unclaimed count (`user.unclaimed`) in your UI
- You need to ensure user data is up-to-date when user returns to the screen

### How to Manually Refresh User Data

Call `memberInfo` API when you need fresh data. This applies to all SDK session start methods:

**Callback version:**
```kotlin
override fun onStart() {
    super.onStart()

    // Manually refresh user data if needed
    RakutenReward.memberInfo({ user ->
        // Update your UI with latest user data
        updateUI(user.point, user.unclaimed)
    }, { error ->
        // Handle error 
    })
}
```

**Coroutine version:**
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

## Error Handling

With v8, error handling is simplified:

- **Token expiry**: Handled automatically by the SDK (when using `RewardTokenProvider`)
- **Invalid tokens**: SDK will request new tokens through your provider

You only need to handle business logic errors specific to your application.  

---
LANGUAGE :
> [![ja](../lang/ja.png)](../ja/migration/v8-migration.md)