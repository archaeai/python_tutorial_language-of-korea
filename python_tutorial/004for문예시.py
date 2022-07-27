#for문은 반복시킬 때 쓴다
print('###111###')
list1=[1,2,3,4,5]
for i in list1:
    print(i)
print('###222###')
cha1='apple'
for i in cha1:
    print(i)
print('###333###')
dic1={'a':1,'b':2,'c':3}
for i in dic1:
    print(i)

"""continue break"""
print('###444###')
for a in list1:
    print(a)
    if a <3:
        continue
    else:
        break
"""break"""
print('###555###')
for a in list1:
    print(a)
    if a >=3:
        break
print('###666###')
for a in list1:
    print(a)
    #break
#for문이 다 실행되면 else가 실행된다.
else:
    print('good boy')
    
