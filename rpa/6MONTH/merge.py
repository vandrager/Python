import os, time, random
from openpyxl import Workbook
wb = Workbook()
ws = wb.active

os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\personal_info")
list_p = os.listdir()
# out_file = open("out.txt", 'w')
print(len(list_p))
ws.append(["name", "age", "e-mail", "division", "telephone", "sex"])
for filename in list_p:
    if ".txt" not in filename:
        continue
    file = open(filename)
    contents = file.readlines()
    list_c = []
    for c in contents:
        cc = c.split(" : ")
        list_c.append(cc[1])
    # out_file.write(content + "\n")
    ws.append(list_c)
    file.close()

# out_file.close()
wb.save("out.xlsx")
    
