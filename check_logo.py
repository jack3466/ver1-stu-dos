import os

# Define the path
folder_path = os.path.join("studos", "static", "images")

print("\n--- CHECKING FOLDER: " + folder_path + " ---")

if os.path.exists(folder_path):
    files = os.listdir(folder_path)
    if not files:
        print("❌ The folder is EMPTY.")
    else:
        for file in files:
            print(f"📁 FOUND FILE: '{file}'")
            
            if file == "logo.png.png":
                print("   ⚠️  PROBLEM FOUND: Double extension!")
                new_name = os.path.join(folder_path, "logo.png")
                old_name = os.path.join(folder_path, file)
                os.rename(old_name, new_name)
                print("   ✅  FIXED: Renamed to 'logo.png'")
            
            elif file == "logo":
                print("   ⚠️  PROBLEM FOUND: No extension!")
                new_name = os.path.join(folder_path, "logo.png")
                old_name = os.path.join(folder_path, file)
                os.rename(old_name, new_name)
                print("   ✅  FIXED: Renamed to 'logo.png'")
                
            elif file == "logo.png":
                print("   ✅  Perfect! This file name is correct.")
else:
    print("❌ CRITICAL: The folder 'studos/static/images' does not exist.")

print("----------------------------------------------\n")