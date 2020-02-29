from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

url = "http://finance.naver.com/sise/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")

# print('soup',soup.prettify())

top = soup.select("#siselist_tab_0 > tr")
#선택자의 활용능력에 따라 다름

i=1
for e in top:
    # print(e)
    # print(e.find("a"))
    if e.find("a") is not None:
        print(i,e.select_one(".tltle").string)
        i += 1

print("----------------------------------------------------------------------------------")
#현재는 네이버의 주식 페이지에 서 상위 10개가 아닌 4개만 나오도록 되어있어서 강의와는 다르게 4개까지만 출력이 됩니다.
#2019.12.12 일 현재 결과
# 1 삼성출판사
# 2 컨버즈
# 3 앤유엔터테인먼트
# 4 노드메이슨
#결과는 크롤링 하는 순간마다 값이 다를 수 있음

#네이버 또한 기존의 주식사이트가 ajax방식으로 변경됨으로 인해 코드 를 수정함

top10 = soup.select("#popularItemList > li > a")

#파싱 확인
# print(top10)

print('네이버 주식 인기검색 종목 10위')
for i, e in enumerate(top10, 1):
    print('순위 : {}, 이름 : {}'.format(i,e.string))
#enumerate 함수
#리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
#열거하다 라는 듰으로 이함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴함
#보통 for문과 함께 자주 사용함
#반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할때 사용함
