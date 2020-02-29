import sys
import io
import requests

#Respinse 상태코드
s = requests.Session()
r = s.get('http://httpbin.org/get')
print(r.status_code)
print(r.ok)

#https://jsonplaceholder.typicode.com

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
# print(r.text)
print(r.json())
print(r.json().keys())
print(r.json().values())
print(r.encoding)
print(r.content)    #바이너리 형태로 정보를 가저옴
print(r.raw)    #로우데이터 형태로 가져옴
