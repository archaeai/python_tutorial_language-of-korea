"""
if 조건:
    조건이 맞다면 실행할 코드
else:
    조건이 다르면 실행할 코드
"""
print('###111###')
list=['a','b','c']
if 'd' in list:
    print('list에 a가 있음')
# else조건이 필요없으면 안써도 된다.
# in은 뒤에 요소가 앞의 요소를 포함하는 지 확인 할 때 쓰는 키워드.
else:
    print('안사요')

print('###222###')
x=3
y=100
if x>y:
    print('omg')
else:
    print('gmo')



"""elif는 조건을 추가하고싶을 때 쓴다
if 조건:
    실행코드
elif 조건:
    실행코드
elif 조건:
    실행코드
...

else:
    실행코드
"""
print('###333###')
x=3

if x==1:#if 조건에서는 ==를 쓴다.
    print('x=1')
elif x==3:
    print('omg')
else:
    print('gmo')

"""if문에 조건을 두개 
if 조건 and,or 조건"""
print('###444###')
m=1
n=1
if m==0 or m==3:
    print('omg')
else:print('gmo')

print('###555###')

if m==1 and n==1:
    print('gmo')
    






