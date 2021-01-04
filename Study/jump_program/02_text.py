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

# 프렌즈 스크립트 가져오기
# https://fangj.github.io/friends/

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
print(re.match(pattern, script)) # script에서 pattern을 찾으세요
# match는 대문자와 소문자를 구분한다.
# 텍스트 중간에 있는 패턴은 찾지 못한다.
print(re.match(pattern, script).group()) # group메서드를 사용해 매치된 내용을 반환합니다.

def refinder(pattern, script):
    if re.match(pattern, script):
        print("match!")
    else:
        print("not match!")

refinder(pattern, script)
pattern = 'is'
script = 'life is so cool'
print(re.search(pattern, script).group())
# match는 찾지 못하지만 search는 텍스트 중간에 있는 텍스트를 찾을 수 있다.


# 패턴을 찾는 정규표현식
# \d = 숫자와 매치, 0-9와 같습니다.
# \D = 숫자가 아닌 것과 매치, [^0-9]와 같습니다.
# \s whitespace 문자와 매치, \t\n\r\f\v와 같습니다. 맨 앞의 빈칸은 공백을 의미합니다.
# \S whitespace 문자가 아닌 것과 매치, [^\t\n\r\f\v]와 같습니다.
# \w 문자 + 숫자와 매치, [a-zA-Z0-9_]와 같습니다.
# \W 문자 + 숫자가 아닌 문자와 매치, [^a-zA-Z0-9_]와 같습니다.
# \\ 메타 문자가 아닌 일반 문자 역슬래시와 매치, 메타 문자 앞에 \를 붙이면 일반 문자를 의미합니다.

number = 'my number is 511333 - 358134 your number is 341539 - 381983'
print(re.findall('\d{6}', number))
a = re.findall('\d{6}', number)
print(a[0] == int)


example = '저는 96년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2021년입니다.'
print(re.findall(r'\d.+년', example))
# 숫자로 시작하고 어떤 숫자든 반복되며 년으로 끝나는 문자열을 반환하라고 명령
# but output = ['96년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2021년'] 탐욕스럽다, 그리디 현상 발생
print(re.findall(r'\d.+?년', example))
# 물음표를 집어넣기, 년이라는 글자를 찾으면 패턴 찾기를 멈춤

example = 'i love my dog, lovely cat, really. i am not telling a lie. what a pretty dog! i love this song'
print(re.split(r'[.?!]', example))
data = 'a:3; b:4; c:5'
for i in re.split(r';', data):
    print(re.split(r':', i))

# sub메서드 문자열 바꾸기 정말 정말 많이 쓰는 것임
# re.sub(찾을 패턴, 대체할 문자, 찾을 문자열)
sentence = 'i love my dog, lovely cat, really. i am not telling a lie. what a pretty dog! i love this song'
print(re.sub(r'dog', 'Fox', sentence))
word = '2pac \n\n\nbiggy \n\n\nkane west'
print(word)
print(re.sub(r'\n', '', word)) #불필요한 부분을 제거해버릴 수 있음! 개꿀!

print(re.findall('\w+?ly', sentence))

import os
import re
print(os.getcwd())

f = open('friend101.txt', 'r', encoding='euc-kr')
script = f.read()
print(script)

line = re.findall(r'Monica:.+', script)
print(line[:3])

for i in line:
    print(i, '\n')


m = open('monica.txt', 'w', encoding='euc-kr')
monica = ''
for k in line:
    monica += k + '\n'
m.write(monica)
print(m)
print(monica)
m.close()

hey = ''
play = str(list(range(1, 11)))
for v in play:
    hey += v

print(hey)

char = re.compile(r'[A-Z][a-z]+:')

# 중복 상관없이 등장인물 이름 모두 출력
print(re.findall(char, script))

# 중복 제거하고 등장인물 이름 모두 출력
y = set(re.findall(char, script))

z = list(y)
print(z)
character = []
for i in z:
    character += [i[:-1]]

print(character)

# set을 통해 중복을 걸러낸 집합은 리스트 형태로 만들어줍시다.
a = {'vain', 'roly', 'poly'}
print(list(a))
print(re.findall(r'\([A-Za-z].+[a-z|\.]\)', script))

# 특정 단어의 예문만 모아 파일로 저장하기
f = open("friend101.txt", 'r')
print(f.read(100))
f.seek(0)
sentence = f.readlines() # 객체 f안의 모든 문장을 원소로 하는 리스트를 만듭니다.
for i in sentence[:20]:
    if re.match(r'[A-Z][a-z]+:', i):
        print(i)

lines = [i for i in sentence if re.match(r'[A-Z][a-z]+:', i)]
print((lines[:10]))

would = [i for i in sentence if re.match(r'[A-Z][a-z]+:', i) and re.search('would', i)]
take = [i for i in sentence if re.match(r'[A-Z][a-z]+:', i) and re.search('take', i)]

for t in take:
    print(t)


newf = open("would.txt", 'w')
newf.writelines(would)
newf.close()

words = ['apple', 'banana', 'cat', 'brave', 'drama', 'arise', 'blow', 'coat', 'abovve']
for i in words:
    m = re.match(r'a\D+', i)
    if m:
        print(m.group())

test = '제 이메일 주소는 vandrager@hanmail.net입니다. 오늘 저는 ybeompark@outlook.kr로 메일을 보내려고 합니다. 작년은 2020년이었고 올해는 2021년입니다'
b = re.findall(r'[a-z]+@[a-z.]+', test)
print(b)

print(re.findall(r'\d+년', test))

d = 'i have dog. i am not a girl. you are not alone. i am happy'
print(re.split('\.', d))