#클래스 - 객체지향
# 객체 - 자동차(실생활에서 눈에 인식할수 있는 사물)
# 클래스(class)
# 필드(속성,변수)
# 메소드(동적- 작업을 수행)
#
# 자동차
# 속성(변수)
# 색,배기량,자동(수동),중형소형,
#
# 메소드
# 전진,후진,왼쪽,오른쪽,방향지시등,라이트

import sys
import io

class UserInfo:
    # def set_info(self, name, phone):
    #__init__ 메소드가 초기 한번실행시에 자동으로 메모리에 올라가도록 함
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("-------------------")
        print("Name = " + self.name)
        print("Phone = "+ self.phone)
        print("-------------------")

    #__del__ 가비지콜렉터가 돌아다니면서 사용하지 않는 메소드를 삭제 하기 전에 마지막으로 한번더 실행되도록함
    def __del__(self):
        print("delete!")

user1 = UserInfo("kim","010-1234-5678")
user2 = UserInfo("park","010-3333-2225")

print(id(user1))
print(id(user2))

# user1.set_info("kim","010-1234-5678")
# user2.set_info("park","010-3333-2225")

user1.print_info()
user2.print_info()

#__dict__ 해당 인스턴스 안에 뭐가 있는지 알아볼수 있다.
print(user1.__dict__)
print(user2.__dict__)

print(user1.phone,user1.name)
