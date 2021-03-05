import time
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Python\chromedriver.exe")
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.current_window_handle
print(curr_handle) # CDwindow-1C6ED033C72EA427A2AFECC2A7990D18

browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()
curr_handle = browser.current_window_handle
print(curr_handle) # CDwindow-0A378F8EB8BAEFCFA1BB7453ACEBF20E

handles = browser.window_handles # 모든 핸들 정보
print(len(handles))
for handle in handles:
    print(handle)
    browser.switch_to_window(handle) # 각 핸들로 이동해서
    print(browser.title)
    print()

# 새로 이동한 브라우저에서 자동화 작업을 수행

# 그 브라우저를 종료
print("현재 핸들 닫기")
browser.close()

# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
browser.switch_to_window(curr_handle)
print(browser.title)