import os
import shutil

# 要整理的資料夾
folder_path = r"C:\Users\燕\Downloads"

# 檔案類型
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "PDF": [".pdf"],
    "Word": [".docx"],
    "Videos": [".mp4"]
}

# 讀取資料夾內所有檔案
for filename in os.listdir(folder_path):

    file_path = os.path.join(folder_path, filename)

    # 跳過資料夾
    if os.path.isdir(file_path):
        continue

    # 取得副檔名
    extension = os.path.splitext(filename)[1].lower()

    # 分類
    for folder_name, extensions in file_types.items():

        if extension in extensions:

            target_folder = os.path.join(folder_path, folder_name)

            # 如果資料夾不存在就建立
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # 移動檔案
            shutil.move(file_path, os.path.join(target_folder, filename))

            print(f"{filename} 已移動到 {folder_name}")