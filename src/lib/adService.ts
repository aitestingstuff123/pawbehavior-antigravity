import { AdMob, RewardAdOptions, RewardAdPluginEvents, PluginListenerHandle } from '@capacitor-community/admob';
import { Capacitor } from '@capacitor/core';

// Store handles globally so we can remove them safely and prevent memory leaks
let rewardListener: PluginListenerHandle | null = null;
let dismissListener: PluginListenerHandle | null = null;
let loadedListener: PluginListenerHandle | null = null;
let failedToLoadListener: PluginListenerHandle | null = null;

const clearListeners = () => {
  if (rewardListener) { rewardListener.remove(); rewardListener = null; }
  if (dismissListener) { dismissListener.remove(); dismissListener = null; }
  if (loadedListener) { loadedListener.remove(); loadedListener = null; }
  if (failedToLoadListener) { failedToLoadListener.remove(); failedToLoadListener = null; }
};

export const rewardedAdService = {
  loadAd: async (
    adId: string, 
    callbacks: { 
      onAdLoaded: () => void, 
      onAdFailedToLoad: (err: any) => void, 
      onUserEarnedReward: () => void 
    }
  ) => {
    try {
      if (!Capacitor.isNativePlatform()) {
        console.log("[AdMob] Running on web. Mocking ad load...");
        setTimeout(() => {
          callbacks.onAdLoaded();
        }, 500);
        return;
      }

      clearListeners(); // Ensure clean slate before loading new ad

      // Await listener attachment to prevent race conditions
      loadedListener = await AdMob.addListener(RewardAdPluginEvents.Loaded, () => {
        callbacks.onAdLoaded();
      });
      failedToLoadListener = await AdMob.addListener(RewardAdPluginEvents.FailedToLoad, (err) => {
        callbacks.onAdFailedToLoad(err);
      });

      const options: RewardAdOptions = {
        adId: adId,
        isTesting: true,
      };

      await AdMob.prepareRewardVideoAd(options);
    } catch (err) {
      console.error("[AdMob] Error loading ad:", err);
      callbacks.onAdFailedToLoad(err);
    }
  },

  showAd: async (
    callbacks: { 
      onUserEarnedReward: (reward: any) => void, 
      onAdClosed: () => void, 
      onAdFailedToLoad: (err: any) => void 
    }
  ) => {
    try {
      if (!Capacitor.isNativePlatform()) {
        console.log("[AdMob] Running on web. Mocking ad playback...");
        // Simulate ad playing for 3 seconds, then grant reward and close
        setTimeout(() => {
          console.log("[AdMob] Web mock ad finished. Granting reward...");
          callbacks.onUserEarnedReward({ amount: 1, type: "test_reward" });
          callbacks.onAdClosed();
        }, 3000);
        return;
      }

      let rewarded = false;

      rewardListener = await AdMob.addListener(RewardAdPluginEvents.Rewarded, (rewardItem) => {
        rewarded = true;
        callbacks.onUserEarnedReward(rewardItem);
      });

      dismissListener = await AdMob.addListener(RewardAdPluginEvents.Dismissed, () => {
        if (!rewarded) {
          // Ad was closed before reward
          callbacks.onAdClosed();
        } else {
          callbacks.onAdClosed();
        }
        // Instead of removing ALL AdMob listeners abruptly, we cleanly remove only ours
        clearListeners();
      });

      await AdMob.showRewardVideoAd();
    } catch (err) {
      console.error("[AdMob] Error showing ad:", err);
      callbacks.onAdFailedToLoad(err);
    }
  }
};
