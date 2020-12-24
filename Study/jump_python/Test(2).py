a = "life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
#가장 먼저 참이 되는 것이 세번째 조건이므로 "shirt"가 출력된다.

i = 0
while True:
    i += 1
    if i > 5: break
    print("*"*i)

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for k in A:
    total += k
average = total/len(A)
print(average)

#리스트의 총 개수를 세어줄 때는 len(리스트명)을 사용한다.