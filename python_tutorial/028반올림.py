#파이썬 내장함수 round()를 이용해서 반올림을 구해보자.
ret1=round(1118)
print(ret1)


#내장함수 없이 반올림을 한다면 어떨까

a=input('일의 자리에서 반올림할 수를 입력하세요 : ')
a=float(a) #입력받는 것들의 타입은 str이고 str은 int로 바로 변경할 수 없기때문에 우선
# float으로 바꾼다음 int로 변경해줬다
a_int=int(a)
if a<a_int+0.5:
    a=a_int
else:a=a_int+1
print('반올림한 %d'%a)
