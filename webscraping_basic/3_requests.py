#pip install requests

import requests
res = requests.get("https://www.google.com/")
res_2 = requests.get("https://www.wavve.com/index.html")
res.raise_for_status() #오류가 발생하면 프로그램을 바로 중단해버림
#request.get과 raise 같은 경우 보통 이렇게 두 줄로 쌍으로 사용한다.

print("응답코드: ", res.status_code) #200이 나오면 정상임ㅋㅋ
print("응답코드: ", res_2.status_code) #응답코드가 403이 나오면 문제가 발생했다는 메시지임

if res.status_code == 200:
    print("정상입니다.")
else:
    print("문제가 발생했습니다.", res.status_code)


print(len(res.text))
with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)