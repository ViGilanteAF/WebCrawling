import sys
import io
import urllib.request as req
from urllib.parse import urlparse

# sys.stdout= io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
# sys.stderr= io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
#https://docs.python.org

url="http://www.encar.com"

mem=req.urlopen(url)

print(type({})) # <class 'dict'>
print(type([])) # <class 'list'>
print(type(())) # <class 'tuple'>

# print("geturl",mem.geturl())
# print("status",mem.status) # 200(normal), 404(noPage), 403(reject), 500(server err)
# print("headers",mem.getheaders())

# print("info",mem.info())
# print("code",mem.getcode())
# print("read",mem.read().decode())
#최신 파이썬은 UTF-8 을 사용하지 않아도 아톰에서는 UTF8 로 인코딩하기 떄문에 UTF-8 을 쓰지 않아도 됩니다.
print(urlparse("http://ww.encar.com?test=test"))

print("download Complete")
