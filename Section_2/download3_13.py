#3vs 가 크롤링에서 가장 중요함
#Volume 데이터의 양
#Variety 데이터의 다양성
#Velocity 데이터의 속도

from bs4 import BeautifulSoup
import urllib.request as req
#주소창 내의 Query 가 바뀌 기 떄문에 Parse 를 같이 import 해줘야함
import urllib.parse as rep
import sys
import io
import os

# opener = req.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# req.install_opener(opener)


base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("걸그룹")
url = base + quote


res = req.urlopen(url)

#경로는 알아서 바꿔야함
savePath = "/Users/stronghu/Documents/inflearn/Section_2/imagedown" #C:/imagedown/

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패!")
        #파이썬 에러처리중 에러를강제적으로 발생시킴
        raise

soup = BeautifulSoup(res,"html.parser")

img_list = soup.select("div.img_area > a.thumb._thumb > img")
# print("test",img_list)

for i, img_list in enumerate(img_list, 1):
    # print(img_list['data-source'])
    #fullFileName변수에 join을 해서 savePath 에 savePath+사진의 갯수만큼 번호가 증가하여 1부터 이름뒤에 스트링형으로 변환하여 붙인뒤 확장자명은 jpg 로 저장하라
    fullFileName = os.path.join(savePath, savePath + str(i) + '.jpg')
    req.urlretrieve(img_list['data-source'],fullFileName)

print("Download Completed")
