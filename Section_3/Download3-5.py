import sys
import io
import requests, json

# r = requests.get('https://api.github.com/events')
# r.raise_for_status()
# print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name','hu',domain = 'httpbin.org',path = '/cookies')

# r = requests.get('https://httpbin.org/cookies',cookies=jar)
# r.raise_for_status()
# print(r.text)


# r = requests.get('https://github.com',timeout=5)#서버응답까지 5초간 대기 하겠음
# print(r.text)

# r = requests.post('http://httpbin.org/post',data={'name':'kim'},cookies=jar)
# print(r.text)

payload1 = {'key1':'value1','key2':'value2'} #dict
payload2 = (('key1','value1'),('key2','value2')) #tuple
#파이썬의 튜블형식 은 한번 결정하면 바꿀수 가 없음
#튜플형식으로 post한걸 폼데이터 형식으로 바꿔서 post함
payload3 = {'some':'nice'}

# r = requests.post('http://httpbin.org/post',data=payload1)
# print(r.text)
#form 데이터로 보냄

r = requests.post('http://httpbin.org/post',data=json.dumps(payload3))
print(r.text)
#json 데이터로 보냄
