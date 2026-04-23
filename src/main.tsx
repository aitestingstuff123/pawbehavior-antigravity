import {StrictMode} from 'react';
import {createRoot} from 'react-dom/client';
import App from './App.tsx';
import './index.css';

import { AuthProvider } from './lib/AuthContext';
import { defineCustomElements } from '@ionic/pwa-elements/loader';
import { AdMob } from '@capacitor-community/admob';
import { Capacitor } from '@capacitor/core';
import { Purchases } from '@revenuecat/purchases-capacitor';

defineCustomElements(window);

// Initialize AdMob
if (Capacitor.isNativePlatform()) {
  try {
    AdMob.initialize({
      requestTrackingAuthorization: true,
      initializeForTesting: true,
    });
  } catch (err) {
    console.error("[AdMob] Failed to initialize:", err);
  }

  // Initialize RevenueCat
  const revenueCatKey = import.meta.env.VITE_REVENUECAT_PUBLIC_KEY;
  if (revenueCatKey) {
    try {
      Purchases.configure({ apiKey: revenueCatKey });
    } catch (err) {
      console.error("[RevenueCat] Failed to initialize:", err);
    }
  } else {
    console.warn("[RevenueCat] Missing VITE_REVENUECAT_PUBLIC_KEY. In-app purchases will not work.");
  }
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <AuthProvider>
      <App />
    </AuthProvider>
  </StrictMode>,
);
