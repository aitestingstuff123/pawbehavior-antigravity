import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.petanalysis.app',
  appName: 'PawBehavior',
  webDir: 'dist',
  server: {
    androidScheme: 'https',
    plugins: {
      SplashScreen: {
        launchShowDuration: 2000,
        launchAutoHide: true,
        backgroundColor: '#09090b',
        androidScaleType: 'CENTER_CROP',
        showSpinner: false,
        splashFullScreen: true,
        splashImmersive: true
      }
    }
  }
};

export default config;
