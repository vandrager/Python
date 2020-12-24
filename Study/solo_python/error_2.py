list_k = [42, 283, 54, 46, 100]

try:
    number_input = int(input("> 정수를 입력하시오. "))
    print("{}번째 요소: {}".format(number_input, list_k[number_input]))
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception", exception)

try:
    number_input = int(input("> 정수를 입력하시오. "))
    print("{}번째 요소: {}".format(number_input, list_k[number_input]))
except ValueError:
    print("아니, 정수를 입력하라니깐?")
except IndexError:
    print("리스트의 인덱스를 벗어났잖아")


try:
    number_input = int(input("> 정수를 입력하시오. "))
    print("{}번째 요소: {}".format(number_input, list_k[number_input]))
except ValueError as e:
    print("아니, 정수를 입력하라니깐?")
    print("exception", e)
except IndexError as e:
    print("리스트의 인덱스를 벗어났잖아")
    print("exception", e)

try:
    number_input = int(input("> 정수를 입력하시오. "))
    print("{}번째 요소: {}".format(number_input, list_k[number_input]))
    예외.발생해주세요()
except ValueError as e:
    print("아니, 정수를 입력하라니깐?")
    print("exception", e)
except IndexError as e:
    print("리스트의 인덱스를 벗어났잖아")
    print("exception", e)
except Exception as exception:
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(exception), exception)

number = input("정수입력> ")
number = int(number)

if number > 0:
    raise NotImplementedError
else:
    raise NotImplementedError