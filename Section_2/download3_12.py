#인프런 또한 강의와는 다르게 소스코드와 홈페이지 레이아웃이 변경이 되어서 강좌를 따라서 하게 되면 작동이 되지 않음!!

from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

base = "http://inflearn.com/"

#주소뒤에 오는 것을 붙여주는 역활을 하며 영문이외의 한글로 되어있을 경우 나 가변적인 값이 올경우 사용함
#현재는 뒤에 붙는 값이 없기 떄문에 아무것도 적지 않음 아래는 강좌를 따라서 만듬
quote = rep.quote_plus("추천-강좌")
# quote = rep.quote_plus("")

url = base + quote

# print(quote)

res = req.urlopen(url).read()

soup = BeautifulSoup(res,"html.parser")
#print(soup)


recommand = soup.select("ul.slides")[0]
# print(recommand)

for i,e in enumerate(recommand,1):
    print(i,e.select_one("h4.block_title > a").string)
    #강좌의 소스코드를 보면 h4 테그의 class명은 block_title 로 된 테그 안에 a테그로 된 titile 를 가지고 오라는 문(현재는 변경되어서 작동하지않음)

#아래의 코드는 작동되지 않는 크롤링을 최대한 비슷하게 만들어둠
# recommand = soup.select("section.inf_slider")[2]
# # print(recommand)
#
# for e in recommand:
#     print(e.select_one("div.card-content > div.course_title").string)
