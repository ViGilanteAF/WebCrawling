import sys
import io

class NameTest:
    total = 0

print(dir())
print("before: ", NameTest.__dict__)
NameTest.total = 1
print("after: ", NameTest.__dict__)

n1 = NameTest()
n2 = NameTest()
print(id(n1)," vs ", id(n2))
#total 의 값은 n1과 n2가 공유하고 있음
print(dir())

print(n1.__dict__)
print(n2.__dict__)
n1.total = 77
print(n1.__dict__) #{'total': 77}
print(n1.total) #77
print(n2.total) #1
#인스턴스 네임스페이스 -> 클래스 네임스페이스 , 클래스 변수(공유)

#print(n1.next) #당연하게도 Error 발생함
