from openpyxl import load_workbook

wb = load_workbook("score_2.xlsx")
ws = wb.active

# 번호, 컴퓨터, 수학
# 번호, (국어), 컴퓨터, 수학

# ws.move_range("B1:C11", rows=0, cols=1) # 열만 오른쪽으로 한 칸 이동
# ws["B1"].value = "국어"
# ws.move_range("B1:C11", rows=0, cols=-1) # 열만 왼쪽으로 다시 한 칸 이동
wb.save("score_2.xlsx")
