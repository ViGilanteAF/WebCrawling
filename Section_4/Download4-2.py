
#html 은 지정된 태그만 사용가능함
#SGML 의 장점과 html 의 장점만으로 WCG에서 표준을 제정한것이 XML
#XML 인터넷 쉽게 , 처리속도 빠르게, 문서작성용이, 가독성이 좋음, 어렵지 않음
#Json 과 더불어 인터넷에서 가장 많이 사용함
#텍스트 + 콘솔: 지역별(최저온도)

import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path

#다운로드 url
url="https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename="/Users/stronghu/Documents/inflearn/WebCrawling/Section_4/forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url,savename)
    print("다운로드 완료되었습니다.")

#BeautifulSoup 파싱
xml = open(savename,'r',encoding="utf-8").read()
soup = BeautifulSoup(xml,'html.parser')

#지역확인
info = {}
for location in soup.find_all("location"):
    #xml 파싱 시에는 find 가 훨신 효율적
    loc = location.find("city").string
    # print(loc)
    weather = location.find_all("tmn")
    # print(weather)
    if not(loc in info): #info 라는 딕셔너리에 loc 가 없으면 info 에 loc 를 선언하고 리스트의 빈값으로 넣어라(중복되지 않음)
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)
# print(info)
# print(sorted(info.keys()))
# print(list(info.keys()))
# print(info.values())

#각 지역별 날씨 텍스트 쓰기
with open ('/Users/stronghu/Documents/inflearn/WebCrawling/Section_4/forest.txt','wt')as f:
    for loc in sorted(info.keys()):
    #list 라고 명시적으로 써주지 않아도 파이썬 에서 자동으로 list 형식으로 해줌
        print("+",loc)
        f.write(str(loc)+'\n')
        for n in info[loc]:
        #딕셔너리 형태의 키값의 리스트가 n을 통해서 순회를 하게됨
            print("-",n)
            f.write('\t'+str(n)+'\n')
            
