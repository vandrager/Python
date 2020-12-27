import pandas as pd
import os
os.chdir('C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Data/practice')
shop = pd.read_csv('shopinfo.csv', header=0, encoding= 'euc-kr')
print(shop.head(5))

#most likely due to a circular import 에러 해결 방법
#문제 원인: 순환 참조 발생
#해결 방법(1): 파일명을 외부 모듈명과 다르게 설정할 것
#조치 결과: 정상 출력, 외부 모듈명과 동일한 파일 순환 참조 중지

keyword = pd.read_csv('2020.12.26_이슈키워드.csv', encoding='euc-kr')
print(keyword)

