from bs4 import BeautifulSoup
import sys
import io

fp = open("/Users/stronghu/Documents/inflearn/Section_2/food-list.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")

print("1",soup.select_one("li:nth-of-type(8)").string)
print("2",soup.select_one("#ac-list > li:nth-of-type(4)").string)
print("3",soup.select("#ac-list > li[data-lo='cn']")[0].string)#list 형태 이기 떄문에 배열로 씀
print("4",soup.select("#ac-list > li.alcohol.high")[0].string)#list 형태 이기 떄문에 배열로 씀


param = {"data-lo": "cn", "class": "alcohol"}
print("5",soup.find("li",param).string)#가독성이 좋은 접근(효율성이 높음)
print("6",soup.find(id="ac-list").find("li",param).string)#부모부터 자식까지 정직하게 접근함(문법적으로 정직하게)

for ac in soup.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us' , ac.string )
