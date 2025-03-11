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

print('address' in name_card)
