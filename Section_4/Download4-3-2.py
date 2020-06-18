#튜플 자료형(순서o, 중복o, 수정x, 삭제x)
#불변 즉 읽기전용으로 최고
#속도 튜플 > 리스트
#인덱싱하는 것은 리스트와 같음 하지만 삭제 는 불가
#따라서 index 와 count  만 지원함
from platform import python_version

#선언
a = () #튜플은 () 임 , 리스트는 []
b = (0,) # 원소를 하나 로 선언시에는 반드시 뒤에 , 를 찎어야함
c = (0,0,1,2) #중복가능, 순서는 유지됨
d = (0,1,'car','apple','apart')
e = (0,1,('car','apple','apart'))

print(type(b))

print('==================================')
print('d - ',type(d),d)
print('d - ',d[1])
print('d - ',d[0]+d[1]+d[1]) #숫자 또는 문자열끼리 연산이 가능함
print('e - ',e[-1][1]) #역순으로 첫번째의 리스트에서 1번째의 값을 가지고 와라 = e[2][1]
print('e - ',e[2][1])


#슬라이싱
print('==================================')
print('d -',d[0:3])
print('d -',d[2:])

#연산
print('==================================')
print('c + d', c+d)
print('c * 3', c*3)
print('hi + c[0]','hi'+str(c[0]))

print(python_version())
