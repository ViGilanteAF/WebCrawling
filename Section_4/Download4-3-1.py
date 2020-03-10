#자료형
#List, Tuple, Dictionary, Sets
a = 'Hello' #문자열

print(type(a)) #string 형인 str 로 나옴
print(a[0]) #리스트 형으로 캐스팅 되어서 가지고옴
print(a[0:3]) #-1 이 되기 때문에 012 의 자리숫자가 나옴
print(a[-1:]) #역순으로 감

# for t in a: #바로 루프문 가능
#     print(t)
#     print(type(t))

#interpreter language = python

#List
#리스트 자료형(순서o, 중복o,수정o, 삭제o)

#선언
a = []
b = list()
c = [0,0,1,2] #중복가능, 순서는 유지됨
d = [0,1,'car','apple','apart']
e = [0,1,['car','apple','apart']]

#인덱싱
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

#리스트 수정, 삭제
print('==================================')
c[0]=4
print('c - ',c)
c[1:2] = ['a','b','c'] #리스트 안에 리스트를 넣은것이 아닌 그냥 추가로 넣은것
print('c - ',c)
c[1] = ['a','b','c']
print('c - ',c) #리스트 안에 리스트를 넣는것
c[1:3] = []
print('c - ',c) # 1:3 까지 다 지워짐
del c[3]    #3번째의 자료를 삭제함
print('c - ',c)

#리스트 함수
print('==================================')
a=[5,2,3,1,4]
print('a - ',a)
a.append(6) #끝에 삽입함
print('a - ',a)
a.sort() #오름차순으로 정렬함
print('a - ',a)
a.reverse() #내림차순으로 정렬함
print('a - ',a)
print('a - ',a.index(4),a[4])
print('a - ',a.count(1)) #똑같은 값이 여러게 있기 때문에 그것에 따른 원소의 갯수 를 셈
a.remove(2) #리스트 안의 원소 2를 지워라
print('a - ',a)
print('a - ',a.pop()) #맨끝의 마지막 원소를 꺼냄
print('a - ',a)
ex = [8,9]
a.extend(ex) #ex의 값을 리스트 맨뒤에 명시적으로 추가하라
print('a - ',a)

#리스트 삭제: del, remove, pop

while a:
     l = a.pop()
     print(l is 4)
