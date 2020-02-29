import io
import sys
import requests

s = requests.Session()
r = s.get('https://www.naver.com') #PUT(FETCH), DELETE, GET, POST
# print('1',r.text)

r = s.get('http://httpbin.org/cookies',cookies={'from':'myName'})
# print(r.text)

url = 'http://httpbin.org/get'

headers = {'user-agent':'myPythonApplication'}

r = s.get(url,headers=headers)
print(r.text)



s.close()

with requests.Session() as s:
    r = s.get('https://www.naver.com')
    print(r.text)
