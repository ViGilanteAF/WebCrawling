import sys
import io
import urllib.request as dw

# sys.stdout= io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
# sys.stderr= io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
#https://docs.python.org

imgUrl="http://blogfiles.naver.net/20160222_233/j_dh1991_1456106505134qdUgn_JPEG/B1A9BFEE_B0EDBEE7C0CC_BBE7C1F8_BDBAC4DA%3FBDAC_C6FAB5E5_7.jpg"
htmlURL="http://google.com"


savePath1="/Users/stronghu/Documents/inflearn/Sectino_2/test1.jpg"
savePath2="/Users/stronghu/Documents/inflearn/Sectino_2/index.html"

dw.urlretrieve(imgUrl,savePath1)
dw.urlretrieve(htmlURL,savePath2)

print("Download Complete")
