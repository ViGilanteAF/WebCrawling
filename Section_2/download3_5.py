from urllib.parse import urljoin
from bs4 import BeautifulSoup
import sys
import io

html ="""
<html><body>
<ul>
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">daum</a></li>
<li><a href="http://www.daum.com">daum</a></li>
<li><a href="http://www.google.com">google</a></li>
<li><a href="http://www.tistory.com">tistory</a></li>
</ul>
<body><html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
# print('links',type(links))
a = soup.find_all("a",string="daum") #포함된 모든 문자열 을 찾음
print('a',a)
b = soup.find("a") #가장 최상위 의 문을 찾음
print('b',b)
c = soup.find_all("a",limit=3) #찾는 제한을 걸음
print('c',c)
d = soup.find_all(string=["naver","google"]) #테그를 가지고 오는것이 아닌 내용을 가지고옴(보통은 정규표현식을 사용함)
print('d',d)
print('d',type(d)) #ResultSet 타입으로 가지고 옴

for a in links:
    # print('a',type(a),a)
    href = a.attrs['href']
    txt = a.string
    # print('txt>>',txt,'href>>',href)
