from urllib.parse import urljoin
from bs4 import BeautifulSoup
import sys
import io

# baseUrl = "http://test.com/html/a.html"
# print(">>",urljoin(baseUrl,"b.html"))
# print(">>",urljoin(baseUrl,"sub/b.html"))
# print(">>",urljoin(baseUrl,"../index.html"))
# print(">>",urljoin(baseUrl,"../img/img.jpg"))
# print(">>",urljoin(baseUrl,"../img/img.css"))

html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>css 선택자</p>
</body>
</html>
"""
soup = BeautifulSoup(html,'html.parser')
# print('soup',type(soup))
print('prettify',soup.prettify)

h1=soup.html.body.h1
print('h1',h1)
print('h1',type(h1))
print(h1.string)

p1=soup.html.body.p
print('p1',p1)

p2 = p1.next_sibling.next_sibling
print('p2',p2)

p3=p1.previous_sibling.previous_sibling
print('p3',p3)


print("h1 >>",h1.string)
print("p1 >>",p1.string)
print("p2 >>",p2.string)
