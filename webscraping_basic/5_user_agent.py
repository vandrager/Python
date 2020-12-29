import requests
url = "https://nadocoding.tistory.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
#user-agent 가져오는 주소는? (https://www.whatismybrowser.com/)
res = requests.get(url, headers = headers)
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)