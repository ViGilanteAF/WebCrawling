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

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb') # w: Warite , r: Read, a: ADD
saveFile1.write(f)
saveFile1.close()


with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)
#with 문 은 Python2.7 이후에 실행이 되며 with 문을 빠저 나오게 되면 자동으로 .Close() 가 됨



print("Download Complete")

#urlretrieve:
#   저장 => open('r') => 변수에 할당 => 파싱 => 저장

#urlopen:
#   변수 할당 => 파싱 => 저장(DB)
