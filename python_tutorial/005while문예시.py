"""for문은 특정범위에서 while 특정조건에서 반복을 실행한다
"""
print('###111###')
x=0
while x<5:
    x=x+1
    print(x)
"""break는 while문을 즉시 종료 continue는 처음으로"""
"""밑에 코드 실행결과는 3이 출력된다. b"""
print('###222###')
x=0
while x<5:
    x=x+1
    if x<3:
        continue
    print(x)
    if x==3:
        break
    print('hahaha')
