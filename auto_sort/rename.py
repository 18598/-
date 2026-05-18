import os

# 資料夾路徑
folder_path = r"C:\Users\燕\Downloads"

# 編號起始
count = 1

# 讀取資料夾內所有檔案
for filename in os.listdir(folder_path):

    # 完整路徑
    old_file = os.path.join(folder_path, filename)

    # 如果是資料夾就跳過
    if os.path.isdir(old_file):
        continue

    # 取得副檔名
    extension = os.path.splitext(filename)[1]

    # 新檔名
    new_name = f"photo_{count}{extension}"

    # 新路徑
    new_file = os.path.join(folder_path, new_name)

    # 改名
    os.rename(old_file, new_file)

    print(f"{filename} → {new_name}")

    count += 1