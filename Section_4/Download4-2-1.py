import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2811062200"
savename = '/Users/stronghu/Documents/inflearn/WebCrawling/Section_4/homeland.xml'

if not os.path.exists(savename):
    req.urlretrieve(url,savename)
    print("다운로드가 완료 되었습니다.")

xml = open(savename,'r',).read()
soup = BeautifulSoup(xml,'html.parser')

info = {}
location = soup.find("category")
for body in  soup.find_all("data"):
    hour = soup.find_all("hour")
    day = soup.find_all("day")
    tmp = soup.find("temp")
    tmx = soup.find_all("tmx")
    tmn = soup.find_all("tmn")
    wfKor = soup.find_all("wfKor")
    wfEn = soup.find_all("wfEn")
    wdKor = soup.find_all("wdKor")
    wdEn = soup.find_all("wdEn")
    reh = soup.find_all("reh")
    if not(body in info):
        info[body] = []
    if not(tmp in info):
        info[tmp]=[]
    for hour in hour:
        info[body].append(hour.string)
    for day in day:
        info[body].append(day.string)
    for tmx in tmx:
        info[body].append(tmx.string)
    for tmn in tmn:
        info[body].append(tmn.string)
    for wfKor in wfKor:
        info[body].append(wfKor.string)
    for wfEn in wfEn:
        info[body].append(wfEn.string)
    for wdKor in wdKor:
        info[body].append(wdKor.string)
    for wdEn in wdEn:
        info[body].append(wdEn.string)
    for reh in reh:
        info[body].append(reh.string)

# with open('/Users/stronghu/Documents/inflearn/WebCrawling/Section_4/homeland.txt','wt')as f:
#     for body in sorted(info.keys()):
#         print("+",body)
#         f.write(str(body)+'\n')
#         for n in info[body]:
#             print("-",n)
#             f.write('\t'+str(n)+'\n')

print(info)
print(sorted(info.keys()))
