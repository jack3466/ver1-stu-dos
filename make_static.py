import os

# Define the path: studos_project/studos/static/images
base_dir = os.getcwd()
path = os.path.join(base_dir, "studos", "static", "images")

# Create the folders
if not os.path.exists(path):
    os.makedirs(path)
    print(f"SUCCESS! Created folder at:\n{path}")
else:
    print(f"Folder already exists at:\n{path}")

print("\n>>> NEXT STEP: Drop your logo.png into this folder!")