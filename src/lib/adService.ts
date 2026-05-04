import { AdMob, RewardAdOptions, RewardAdPluginEvents } from '@capacitor-community/admob';
import { Capacitor } from '@capacitor/core';

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

      AdMob.addListener(RewardAdPluginEvents.Loaded, () => {
        callbacks.onAdLoaded();
      });
      AdMob.addListener(RewardAdPluginEvents.FailedToLoad, (err) => {
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

      AdMob.addListener(RewardAdPluginEvents.Rewarded, (rewardItem) => {
        rewarded = true;
        callbacks.onUserEarnedReward(rewardItem);
      });

      AdMob.addListener(RewardAdPluginEvents.Dismissed, () => {
        if (!rewarded) {
          // Ad was closed before reward
          callbacks.onAdClosed();
        } else {
          callbacks.onAdClosed();
        }
        AdMob.removeAllListeners();
      });

      await AdMob.showRewardVideoAd();
    } catch (err) {
      console.error("[AdMob] Error showing ad:", err);
      callbacks.onAdFailedToLoad(err);
    }
  }
};
