import requests
from bs4 import BeautifulSoup

url = "https://www.koreabaseball.com/Default.aspx"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

beat = soup.find_all("td", attrs={"data-id": "HRA_RT"}).get_text()
# link = beat[0].a["href"]
# print( link)
# print(beat.get_text())
print(beat)