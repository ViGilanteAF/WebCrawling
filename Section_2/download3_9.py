from bs4 import BeautifulSoup
import sys
import io

fp = open("/Users/stronghu/Documents/inflearn/Section_2/cars.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")

def car_func(selector):
    print("car_func",soup.select_one(selector).string)

car_func("#gr")
car_func("li#gr")
car_func("ul > li#gr")
car_func("#cars #gr")
car_func("#cars > #gr")
car_func("li[id='gr']")

print(soup.select("li")[3].string)
print("car_func",soup.find_all("li")[3].string)

#람다식 을 활용하면 코딩을 간결하게 사용이 가능함
car_lambda = lambda q:print("car_lanbda",soup.select_one(q).string)
car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul > li#gr")
car_lambda("#cars #gr")
car_lambda("#cars > #gr")
car_lambda("li[id='gr']")
