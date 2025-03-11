name_card = {'name':'홍길동',
             'tel':'010-888-9999',
             'address':'부산',
             'email':'hong@gmail.com',
             'tel':'000-0000-0000'} # key 값이 같을 때, 뒤에 나온 데이터로 덮어 씌운다

print(name_card)

name_card = {'name':'홍길동',
             'tel':'010-888-9999',
             'address':'부산',
             'email':'hong@gmail.com',
             1.1:'000-0000-0000'} # 실수 값을 key값으로 쓰지 않는다. 되더라도 안쓰는게 좋다.

print(name_card)

name_card = {'name':'홍길동',
             'tel':'010-888-9999',
             'address':'부산',
             'email':'hong@gmail.com',
             [2,1]:'000-0000-0000'} # list는 안된다. 변하는 값을 key로 쓰지 않는다.

print(name_card)

name_card = {'name':'홍길동',
             'tel':'010-888-9999',
             'address':'부산',
             'email':'hong@gmail.com',
             (2,1):'000-0000-0000'} # 튜플은 변하지 않기 때문에 가능하나, 실수값을 key로 쓰지 않기 때문에 되도록이면 사용하지 않도록 한다.

print(name_card)

name_card['etc'] = '이사 갈 수도 있음...' # 없는 값은 추가한다.

print(name_card)

name_card['etc'] = ['이사 갈 수도 있음...','1년 안에'] # 없는 값은 추가한다.

print(name_card['etc'][1]) # 1년 안에 출력

del name_card['address']

print(name_card) # address가 지워졌음.

print(type) # 데이터의 타입이 궁금함 : 딕셔너리

print(len(name_card)) # 안에 있는 요소의 개수 알려줌 : 4개

print('address' in name_card) # 딕셔너리의 특정 key 값이 있는 지 확인 (TRUE / FALSE)

print(name_card.keys()) # 딕셔너리의 key 값만 출력
print(name_card.values)() # 딕셔너리의 values의 값만 출력
print(name_card.items()) # key, values 세트로 출력

list(name_card.keys()) # 딕셔너리의 key 값을 list로 변환

# 따로 작업 하고 싶으면 for 문을 돌린다. 
for k in name_card.keys():
    print(k)

print('-----')

for k in name_card.values():
    print(k)

print('-----')

# items() : (key,value) 튜플 형태로 출력
for k in name_card.items():
    print(k)
print('-----')

# 변수를 두 개로 받으면, 하나씩 맞춰서 출력 => 다른 언어에서는 이게 어렵다. 
    # 주의할 점 : 변수 개수를 맞춰줘야한다. 
for k,v in name_card.items() :
    print(k,v)
print('-----')

name_card.clear() # 딕셔너리 안의 key, value 모든 값을 삭제한다. 
print(name_card) # 딕셔너리 자체는 없애지 않고, 비워주는 역할

print(name_card.get('address')) # find(), index() 그 값이 없으면 오류, -1이 뜬다.


### set 집합함수

s1 = set([1,2,3,3,2])
print(s1) # 중복된 값은 하나로 출력 => key 값을 보여주기 때문에

s2 = set('hello')
print('s2') # 순서가 없기 때문에, h가 먼저 오는 게 아니라 랜덤으로 온다.

# 값 1개 추가하기
s1 = set([1,2,3])
s1.add(4)
print(s1)

# 값 여러 개 추가하기 
s1.update([4,5,6])
print(s1)

# 특정 값 제거하기
s1.remove(2)
print(s1)
