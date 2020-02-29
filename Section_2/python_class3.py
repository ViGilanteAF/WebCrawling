import sys
import io

#ㅡㄹ래스 변수 , 인스턴스 변수

class Warehouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('kim')
user2 = Warehouse('park')

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)
#{'__module__': '__main__', 'stock_num': 2, '__init__': <function Warehouse.__init__ at 0x101acb440>, '__del__': <function Warehouse.__del__ at 0x101b190e0>, '__dict__': <attribute '__dict__' of 'Warehouse' objects>, '__weakref__': <attribute '__weakref__' of 'Warehouse' objects>, '__doc__': None}
#stock_num 이 2 가 된걸 볼 수 있는데 이는 인스턴스를 생성하는 시점에 클래스의초기화 함수가 호출시점에 stock_num 의 변수의 값을 두번 증가 시켰기 때문에 2가 된것

print(user1.stock_num)
print(user2.stock_num)
#2 가 2번 나온걸 볼수 있음

#클래스 변수 는 공유가 되지만 자기 인스턴스 변수는 공유가 되지 않는다 하지만 접근은 가능하다.
#처음에는 자신의(인스턴스) 네임스페이스를 확인하고 그다음에 클래스의 네임스페이스를 확인하여 호출을 함
#클래스 변수는 서로 공유가됨
