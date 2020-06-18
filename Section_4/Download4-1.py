import pickle #(객체, 텍스트)직렬화, 역직렬화

# 파일 이름과 데이터
bfilename = '/Users/stronghu/Documents/inflearn/WebCrawling/test.bin'
tfilename = '/Users/stronghu/Documents/inflearn/WebCrawling/test.txt'

data1=77
data2="Hello, world!"
data3 = ["car","apple","house"]

#바이너리 쓰기
with open(bfilename, 'wb')as f:
    pickle.dump(data1,f)
    #dump 는 객체를 직렬화 할때 사용함
    #dumps는 그냥 텍스트(문자열)를 직렬화 할때 사용함
    pickle.dump(data2,f)
    pickle.dump(data3,f)

#텍스트 쓰기
with open(tfilename,'wt')as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    #f.write(data3)
    #data3는 리스트 로 선언되어있기 때문에 파이썬에서는 , 나 엔터를 구분할수가 없기때문에 따로 메소드를 지원함
    f.writelines('\n'.join(data3))
        

# 바이너리 읽기
with open(bfilename,'rb') as f:
    b = pickle.load(f)
    #load 는 객체를 역직렬화 즉 객체를 불러와서 그대로 보여주는것
    #loads 는 문자열을 읽어 오는 것
    print(type(b),' Binary Read1 | ',b)
    b = pickle.load(f)
    print(type(b),' Binary Read2 | ',b)
    b = pickle.load(f)
    print(type(b),'Binary Read3 | ',b)

    # <class 'int'>  Binary Read1 |  77
    # <class 'str'>  Binary Read2 |  Hello, world!
    # <class 'list'> Binary Read3 |  ['car', 'apple', 'house']


    #pickle 를 잘활용을 하면 윈도우나 맥에서 전용프로그램 제작시 중요데이터나 암호값을 바이너리 형태로
    #저장하고 불러오는 것을 할 수 있게됨

    #텍스트 읽기
    with open(tfilename,'rt')as f:
        for i,line in enumerate(f,1):
            print(type(line),'Text Read'+str(i)+'|' ,line,end='')
            #문자+문자는 문자로 변환해준다. , print 에서는 end='' 를 사용하면 마지막에 같이 출력이 된다.
