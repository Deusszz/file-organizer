import os
import shutil

print("Starting file organizer...")

downloads_path = "C:/Users/third/Downloads"

print("Organizing files...")

for file_name in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, file_name)

    print(f"Found: {file_name}")  

    if os.path.isdir(file_path):
        print("⤵️ Skipping folder")
        continue

    file_ext = os.path.splitext(file_name)[1].lower()

    if file_ext:
        folder_name = file_ext[1:].upper() + "_Files"
    else:
        folder_name = "No_Extension"

    # Sanitize folder name just in case
    folder_name = "".join(c for c in folder_name if c.isalnum() or c in "_- ")

    folder_path = os.path.join(downloads_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    try:
        new_file_path = os.path.join(folder_path, file_name)
        shutil.move(file_path, new_file_path)
        print(f"✅ Moved {file_name} → {folder_name}")
    except Exception as e:
        print(f"❌ Error moving {file_name}: {e}")


