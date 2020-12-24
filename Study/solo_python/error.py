print("프로그램이 시작되었습니다.")
print("프로그램이 시작되었습니다.")
list_a = [1, 2, 3, 4, 5]
print(list_a[1])
input_a = input("> 정수 입력: ")
if input_a.isdigit():
    number_input_a = int(input_a)
    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", 2 * 3.14 * number_input_a)
    print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
else:
    print("정수를 입력하지 않았습니다.")

try:
    number_input_a = int(input("> 정수 입력: "))
    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", 2 * 3.14 * number_input_a)
    print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
except:
    print("무언가 잘못되었습니다.")

list_input_a = ["52", "273", "32", "스파이", "103"]
list_num = []
for item in list_input_a:
    try:
        float(item)
        list_num.append(item)
    except:
        pass

print(list_num)

try:
    number_input_a = int(input("> 정수 입력: "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", 2 * 3.14 * number_input_a)
    print("원의 넓이: ", 3.14 * number_input_a * number_input_a)


try:
    number_input_a = int(input("> 정수 입력: "))
    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", 2 * 3.14 * number_input_a)
    print("원의 넓이: ", 3.14 * number_input_a * number_input_a)
except:
    print("정수를 입력해달라고 했잖아...")
else:
    print("\"예외가 발생하지 않았습니다^^\"")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다...")

numbers = [52, 273, 32, 103, 90, 19, 275]
print("#(1) 요소 내부에 있는 값 찾기")
print(" - {}는 {}위치에 있습니다.".format(52, numbers.index(52)))
print()

print("#(2) 요소 내부에 없는 값 찾기")
number = 32
try:
        print(" - {}는 {}위치에 있습니다.".format(number, numbers.index(number)))
except:
    print(" - 리스트 내부에 없는 값입니다.")
print()

print("--- 정상적으로 종료되었습니다. ---")

print("output = 10 + 개")
print("int(안녕하세요)")
print("cursor.close()")
[1, 2, 3, 4, 5][4]
