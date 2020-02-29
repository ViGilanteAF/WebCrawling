import sys
import io


class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")


f = SelfTest()
print(dir(f))
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'function1', 'function2']
#맨뒤에 function1,function2 가 있는걸 볼 수 있다.

# f.function1()
#자동으로 뭔가가 넘어간다고 생각해야됨

print(id(f)) #메모리 주소가 나옴
f.function2() #22번 줄의 값과 같음 그 이유는 자동으로 인스턴스 주소값이 self에 담겨서 넘어간다고 보면됨

print(SelfTest.function1())#인스턴스 화 시키지않고 클래스의 네임 그대로 직접적으로 호출하면 정상적으로 호출이 됨
