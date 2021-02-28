from openpyxl import Workbook
from random import *
wb = Workbook()
ws = wb.active

# 1줄씩 데이터 넣기
ws.append(["번호", "영어", "수학"])
for i in range(1, 11):
    ws.append([i, randint(0, 100), randint(0, 100)])

col_b = ws["B"] # 영어 컬럼만 가지고 오기
print(col_b)
for c in col_b:
    print(c.value)

col_range = ws["B:C"] # 영어, 수학 컬럼 함께 가지고 오기
for r in col_range:
    for c in r:
        print(c.value)

row_title = ws[1] # 1번째 로우만 가지고 오기

for r in row_title:
    print(r.value)

row_range = ws[2:6] # 1번째 로우는 제외하고 2번째에서 6번째 줄까지 가지고 옴

for r in row_range:
    for c in r:
        print(c.value, end = " ")
    print()
from openpyxl.utils.cell import coordinate_from_string # 좌표정보를 가져오고 싶다면 사용
row_range = ws[2:ws.max_row] # 1번째 로우는 제외하고 마지막 줄까지 가지고 옴

for r in row_range:
    for c in r:
        print(c.coordinate, end = " ")
        xy = coordinate_from_string(c.coordinate)
        print(xy, end = " ")
    print()
wb.save("score.xlsx")


