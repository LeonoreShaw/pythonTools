# coding:utf-8
# 导入os库
import os

# 图片存放的路径
path = r"C:\Users\Michael\Desktop\speed\speed60"

# 遍历更改文件名
num = 1
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,"speed60num"+str(num))+".jpg") #  自定义重命名格式
    num = num + 1
