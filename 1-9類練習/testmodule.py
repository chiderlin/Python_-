#載入內建的sys模組並取得資訊
# import sys # as s 別名

#調整搜尋模組的路徑
# import sys 
# print(sys.path)
# print(sys.platform)
# print(sys.maxsize)
# print(dir(sys)) #顯示模組所有可用的方法，可以用在各個套件中!
# sys 模組是關於系統的模組,屬於cmd與python之間的連結


# 複製,移動,刪除,新增目錄,檔案
# 屬於外部檔案與python之間的互動
import os
# print(dir(os))
# if not os.path.isdir('./data/'):
#     print("無此目錄(資料夾)")
# os.mkdir('./data/') # 新增目錄
# os.makedirs("./data/test/play/test/") #新增多層目錄 
# os.rmdir('./data/') #只能刪除單層空目錄

import shutil
# shutil.rmtree("./data/") #可以一併刪除資料夾+裡面的內容檔
# shutil.copyfile("a601.py","aa601.py") #當前檔案複製
# shutil.move("./data","../") #當前位置資料夾移到上一層(桌面)

#../ 指上一層
#./ 指當前目錄位置