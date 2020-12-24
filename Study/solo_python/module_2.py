from bs4 import BeautifulSoup
from urllib import request

target = request.urlopen("http://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp")
soup = BeautifulSoup(target, "html.parser")
print(target)

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1>hello world!</h1>"