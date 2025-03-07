a = [1,2,3,['abbb','b',[1,3,5],'c']]
print(a)
print(type(a))
print(a[0])
print(a[3][1])
print(a[3][2][1:])

# split은 list로 출력
jumin = '000212-4444444'
print(jumin.split()) # list로 출력

# 리스트 연산하기 (*, + 가능)


# 리스트 길이 
print(len(jumin))
print(len(a))
print(len(a)[3])
print(len(a[3][0]))

a[3][0] = 'hi'
print(a)

del a[3]
del a
# print(a) # a가 정의되지 않다고 에러가 뜬다. 즉, del에서 a를 삭제했음을 알 수 있다. 

a = [1,2,3]
a.append('qqq') # 덧붙이다, 마지막에 특정값을 추가한다. 추가하고 싶은 모든 값(형태) 다 받을 수 있다. 
print(a)
a.insert(0,'aaa') # 원하는 위치값을 지정해서 추가할 수 있다. 
print(a)

a=[1,4,3,2]
a.sort(reverse=True) # defualt는 reverse = Flase : 오름차순 
print(a)

a=[2,3,4,1]
a.reverse()
print(a)

a = ['a','b','c','b']
a.remove('b') # 처음 나오는 해당 값을 지워준다.
print(a)
# 누가 지워졌는지, 해당 회원 값을 찾아서 출력해주지 못한다. 
# remove는 지우기 전에, 어떤 값을 지우는지 찾아서 출력한 후 remove 하면 지워준다. 
# pop은 return 해주고 지운다. 

a = ['a','b','c','b']
a.index('b')
print(a.pop(a.index('b'))) # return 값 존재함
print(a)

# tuple 자료형
t1 = (1,2,'a','b')
t1[0] = 0 # 순서가 있기 때문에 인덱싱은 가능하나, 기존 것을 바꾸는 것은 안된다. 
del t1 # 전체 삭제 가능
print(t1)

t1 = (1,2,'a','b')
del t1[0] # 부분 삭제 불가능