from bs4 import BeautifulSoup
import sys
import io
import re #regex

html ="""
<html><body>
<ul>
<li><a id = "naver" href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">daum</a></li>
<li><a href="http://www.daum.com">daum</a></li>
<li><a href="https://www.google.com">google</a></li>
<li><a href="https://www.tistory.com">tistory</a></li>
</ul>
<body><html>
"""

soup = BeautifulSoup(html,'html.parser')
print(soup.find(id="naver").string)
li = soup.find_all(href=re.compile(r"^https://"))#정규표현식의 형태로 'Row' 데이터의 형태의 시작은 'https://' 이걸로 되어야 한다.
# li = soup.find_all(href=re.compile(r"^daum""))
# print('li',li)
for e in li:
    print(e.attrs['href'])
