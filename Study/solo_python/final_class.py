def sum(a, b):
    return print(a + b)

sum(15, 35)

def problem(issue, maker):
    count = maker * issue * 3
    if count > 30:
        print("학교가 징계를 받습니다.")
    elif 15 < count <= 30:
        print("학교가 징계받을 위험 수준입니다.")
    else:
        print("학교가 징계받지 않습니다.")

problem(5, 1)