from selenium import webdriver
options = webdriver.ChromeOptions()
options.headless =  True
options.add_argument("window-size=1920-1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.maximize_window()


# Headless 사용시 에러메시지 출력 Why..?
# Exception has occurred: WebDriverException
# Message: unknown error: Chrome failed to start: was killed.
#   (unknown error: DevToolsActivePort file doesn't exist)
#   (The process started from chrome location C:\Program Files\Google\Chrome\Application\chrome.exe is no longer running, so ChromeDriver is assuming that Chrome has crashed.)
#   File "C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Python\webscraping_basic\17_chrome_headless.py", line 7, in <module>
#     browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)

# 셀리니움 더 공부하고 싶다면..??
# --> https://selenium-python.readthedocs.io/ 사이트 참고!
# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)


# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내림

prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("googlemovie.png")

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()