# 폴더 안에 폴더 만들기
import os
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata")


for i in range(6):
    os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata")
    os.mkdir(f"folder_{i}")
    os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\folder_{}".format(i))
    os.mkdir(f"give_test{i}")
    os.mkdir(f"get_test{i}")
    os.mkdir(f"yes_test{i}")