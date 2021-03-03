from openpyxl import Workbook
from openpyxl.drawing.image import Image
import pandas as pd
wb = Workbook()
ws = wb.active

# img = Image("img.png")

# ws.add_image(img, "C3")

# # import error you must install Pillow to fetch image...
# # pip install pillow
# wb.save("sample_image.xlsx")

# quiz
# from openpyxl import load_workbook
# wb = load_workbook("data.xlsx")
# ws = wb.active

# for row in ws.iter_rows(min_row = 2, min_col = 2, max_col = 2): # 전체 row 슬라이싱
#     row = 10

# ws['H1'] = "총점"
# ws['I1'] = "성적"

# for row in ws.iter_rows(min_row = 2, min_col = 8, max_col = 8): # 전체 row 슬라이싱
#     row = "=SUM(A:G)"


# wb.save("scores.xlsx")

# 판다스로 함 해볼까
df = pd.read_excel("data.xlsx")
df['총점'] = 0
df['성적'] = 0
df.columns = ["학번", "출석", "퀴즈1", "퀴즈2", "중간고사", "기말고사", "프로젝트", "총점", "성적"]
df['퀴즈2'] = 10
for i in range(len(df['총점'])):
    sum_value = df['출석'][i] + df['퀴즈1'][i] + df['퀴즈2'][i] + df['중간고사'][i] + df['기말고사'][i] + df['프로젝트'][i]
    df['총점'][i] = sum_value
    if df['출석'][i] < 5:
        df['성적'][i] = "F"
    elif sum_value >= 90:
        df['성적'][i] = "A"
    elif sum_value >= 80:
        df['성적'][i] = "B"
    elif sum_value >= 70:
        df['성적'][i] = "C"
    else:
        df['성적'][i] = "D"
# 1. 퀴즈2 점수를 10 으로 수정
# 2. H열에 총점(SUM 이용), I열에 성적 정보 추가
# - 총점 90 이상 A, 80 이상 B, 70 이상 C, 나머지 D
# 3. 출석이 5 미만인 학생은 총점 상관없이 F
df.to_excel("scores.xlsx")