#정규식
#주민등록번호
#960201- 164223*

#이메일 주소
#vandrager@yahoo.com

import re

#abcd, #book #desk
#ca?e
#care, cafe, cave

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case | caffe
# ^(^de): 문자열의 시작 > desk, destination (O) fade (X)
# $ (se$): 문자열의 끝 > case, vase (O) | face(X)


m = p.match("case")
#매치되지 않으면 에러가 발생

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")

m = p.match("careless")
# match: 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)