#기존 Daum 주식 사이트 크롤링

# from bs4 import BeautifulSoup
# import urllib.request as req
# import sys
# import io
#
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#
# url = "http://finance.daum.net/quote/kospi.daum?nil_profile=stocktop&nil_menu=nstock27"
# res = req.urlopen(url).read()
# soup = BeautifulSoup(res, "html.parser")
#
# top = soup.select("ul#myListTop1 > li")
#
# for i,e in enumerate(top,1):
#     print(i,e.find("a").string, "=", e.find("span").string)

#기존 Daum 주식 사이트 : ajax 방식으로 변경으로 인해 코드수정
#pip install fake-useragent 설치 후 실행 됨

import io
import json
import sys
import urllib.request as req

from fake_useragent import UserAgent

#Fake Header 정보
ua = UserAgent()

#헤더 선언
headers = {
    'User-Agent':ua.ie,
    'referer':'https://finance.daum.net/'

}

#다음 주식 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"

res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

# print('res'.res)

rank_json = json.loads(res)['data']

print('중간 확인:', rank_json, '\n')

for elm in rank_json:
    # print(type(elm))
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'],elm['tradePrice'],elm['name']),)
