import urllib.request as urllib

pit = urllib.urlopen('https://comic.naver.com/index.nhn')
print(pit.read().decode('utf-8'))