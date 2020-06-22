import os
path=r"D:\softinstall"
for fpath,dirname,fname in os.walk(path):
    print(fpath)##所有文件夹路径,所有文件夹，所有文件名

