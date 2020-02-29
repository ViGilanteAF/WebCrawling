import io
import sys
import requests, json


#Rest : POST, GET, PUT:UPDATE, REPLACE (FETCH : UPDATE, MODIFY), DELETE

payload1 = {'key1':'value1','key2':'value2'} #dict
payload2 = (('key1','value1'),('key2','value2')) #tuple
payload3 = {'some':'nice'} #json

# r = requests.put('http://httpbin.org/put',data = payload1)
# print(r.text)

# r = requests.put('https://jsonplaceholder.typicode.com/posts/1',data=payload1)
# print(r.text)
#서버가 우리가 보넨 데이터를 1번 ID 값을 가지고 등록을 했다고 답해줌

# r = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
# print(r.text)

r = requests.get('http://ws.bus.go.kr/api/rest/stationinfo/getStationByName?stSrch=',data = '%ea%b0%80%ea%b3%a1%ec%b4%88%ea%b5%90')
print(r.text)
