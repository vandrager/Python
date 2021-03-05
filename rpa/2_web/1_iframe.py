# 프레임이란?
# <iframe> 태그는 인라인 프레임(inline frame)을 정의할 때 사용합니다.

# 인라인 프레임은 현재 HTML 문서에 다른 문서를 포함시킬 때 사용합니다.

# <iframe> 요소의 시작 태그와 종료 태그 사이에는 <iframe> 요소를 지원하지 않는 브라우저를 위한 텍스트를 포함할 수 있습니다.
'''
<html>
    <body>
        <iframe id = "1">
            <html>
                <body>
                    <div ...>
                </body>
            </html>
        </iframe>
        <iframe id = "2">
            <html>
                <body>
                    <div ...>
                </body>
            </html>
        </iframe>
    </body>
</html>
'''

import time
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Python\chromedriver.exe")

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

# elem = browser.find_element_by_xpath('//*[@id="male"]')
# Message: no such element: Unable to locate element:

# <iframe frameborder="0" id="iframeResult" name="iframeResult" allowfullscreen="true"></iframe>
browser.switch_to.frame("iframeResult") # 프레임 전환을 하겠다. frame id명을 넣어주자
elem = browser.find_element_by_xpath('//*[@id="male"]')
elem.click()
interval = 3

browser.switch_to.default_content() # 상위로 빠져나가기
time.sleep(interval)