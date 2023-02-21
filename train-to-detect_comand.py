import pathlib
from pathlib import Path
import datetime
import os
import shutil


work_path = pathlib.Path().absolute()
print(work_path)
time = datetime.datetime.now()
time_name = "{0:%Y%m%d_%H%M%S}".format(time)

# #学習用フォルダのバックアップと新規作成
# train_path = pathlib.Path('./data/train')
# train_path.rename(pathlib.Path('./data/' + time_name + "_train"))
# pathlib.Path('./data/train').mkdir()
# valid_path = pathlib.Path('./data/valid')
# #valid_path.rename(pathlib.Path('./data/' + time_name + "_valid"))

# #出力されたデータを検索し、学習用フォルダへ移動
# output_file = Path('./runs/detect/')
# files = list(output_file.glob("*"))
# file_updates = {file_path: os.stat(file_path).st_mtime for file_path in files}
# newst_file_path = max(file_updates, key=file_updates.get)
# print("NEW",newst_file_path)
# shutil.move(os.path.join(str(newst_file_path) + "/images"),("./data/train/"))
# shutil.move(os.path.join(str(newst_file_path) + "/labels"),("./data/train/"))

#推論用のコマンド作成
weight_file = Path('./runs/train/')
files = list(weight_file.glob("*"))
file_updates = {file_path: os.stat(file_path).st_mtime for file_path in files}
newst_weight_path = max(file_updates, key=file_updates.get)
print("NEW",newst_weight_path)
weight_path = str(newst_weight_path)
input_comand = "python3 detect_output_to_train.py --weights " + weight_path + "/weights/best.pt --source camera2_20220531_master.mp4 --save-txt --save-conf --view-img"
with open('detect_output_to_train.sh', 'w') as f:
    f.write(input_comand)

print("NEXT_STEP: detect_output_to_train.shの内容をターミナルにて実行")