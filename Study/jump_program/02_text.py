import os
import re
print(os.getcwd()) # 현재 작업 폴더
os.chdir("C:/Users/vandr/OneDrive/바탕 화면/Design") # 작업 폴더 변경
print(os.getcwd())
os.chdir("C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Python/Study/jump_program") # 작업 폴더 원위치
# 꿀팁!! 슬래시를 변경하지 않고 폴더 위치 앞에 r을 붙이면 \를 특수문자로 인식하지 않아 정상적으로 이동된다.
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Design\미디어\한국영화")
print(os.getcwd())
os.chdir("C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Python/Study/jump_program")


# 파일 열고 닫기
# open은 파일을 여는 함수
# close는 파일을 닫는 함수

f = open("a.txt", 'w')
open("a.txt", 'w').write('abc')
f.close()

# 파일 열기 모드
# 'w' 파일에 내용을 새로 쓸 때 사용
# 'r' 파일 내용을 읽을 때 사용
# 'a' 파일에 내용을 추가할 때 사용
print(open("a.txt", 'r').read())
f = open("a.txt", 'a')
f.write("나는 할 수 있다.")
f.close()
print(open("a.txt", 'r').read())

# with문으로 객체를 만들지 않고 파일 입출력하기
# f = open ... 이런식으로 만들면 객체명 기억해야하고 open, close를 수시로 해야해서 매우 귀찮아지고 복잡하다.

with open('a.txt', 'w') as v:
    v.write('내 몸을 삼키다.')

f = open("한글파일.txt", 'r', encoding='utf-8')
script = f.read()
print(script)
# 한글 파일로 만들고 인코딩 설정 안하면 아래와 같은 코덱 문제 발생
# UnicodeDecodeError: 'cp949' codec can't decode byte 0xed in position 0: illegal multibyte sequence


pattern = r'life'
script = 'life'
print(re.match(pattern, script))
print(re.match(pattern, script).group())