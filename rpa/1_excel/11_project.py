from openpyxl import Workbook
import random, os
wb = Workbook() # 새 워크북을 생성
ws = wb.active # 현재 활성화된 sheet를 가져옴
ws.title = "project" # 시트 이름 변경
ws.sheet_properties.tabColor = "ffffff" # RGB 형태로 값을 넣어주면 탭 색상 변경


ws.append(["ID", "이름", "이메일", "지역", "기본점수", "추가점수", "종합점수"])

NUM_SAMPLES = 100
alphabet_samples = "abcdefghizklmnopqrstuvwxyz"


# 무작위로 선택된 영어 글자를 생성
def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabet_samples)
    return result


# 이름 생성에 사용할 샘플 글자 정의
first_name_samples = "김이박최정강조윤장임한오서신권황안송전홍유고문양손배조백허유남심노정하곽성차주우구신임전민유류나진지엄채원천방공강현함변염양변여추노도소신석선설마길주연방위표명기반라왕금옥육인맹제모장남궁탁국여진어"
middle_name_samples = "이우리실현에두다천고에청춘의열락의인생에바이며아름다우냐?청춘은풍부하게청춘의천고에위하여서품었기청춘의이상은말이다위하여끓는듣기만속에사랑의우리의붙잡아두기그리무한한있다"
last_name_samples = "작고대한커다란칼이다붙잡아보이는군영과평화스러운것이다귀는수무엇을노년에게서갑날카로우나가슴에품고사막이다충분히예가곳으로기쁘며미인을같으며못할위하여서할지니풀이가는뜨고보내는보라"


# 무작위로 사람 이름을 생성하는 함수
def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result





for i in range(NUM_SAMPLES):
    ids = i+1
    name = random_name()
    mail = random_string(8) + "@naver.com"
    location = random.choice(["서울", "경기", "충청", "강원", "경상", "전라", "제주", "인천"])
    basic = random.randint(0, 100)
    plus = random.randint(0, 10)
    total = basic + plus
    ws.append([ids, name, mail, location, basic, plus, total])



wb.save("project.xlsx")

