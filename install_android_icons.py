import os
from PIL import Image

# Path to the generated luxury icon
source_icon = r"C:\Users\ok\.gemini\antigravity\brain\a39df8cc-d927-433e-a255-47325b2e4ebd\pawbehavior_luxury_icon_1776917736734.png"
android_res_dir = r"c:\Users\ok\Downloads\pawbehavior (1)\android\app\src\main\res"

sizes = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192
}

def create_icons():
    if not os.path.exists(source_icon):
        print(f"Source icon not found: {source_icon}")
        return

    img = Image.open(source_icon)
    
    for folder, size in sizes.items():
        target_dir = os.path.join(android_res_dir, folder)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        # Standard icon
        icon_path = os.path.join(target_dir, "ic_launcher.png")
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        resized_img.save(icon_path)
        
        # Round icon
        round_icon_path = os.path.join(target_dir, "ic_launcher_round.png")
        resized_img.save(round_icon_path)
        
        print(f"Created icon in {folder}")

if __name__ == "__main__":
    create_icons()
    print("Android icon installation complete.")
