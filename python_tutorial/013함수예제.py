def str_add(t1,t2='hi'):
    print(t1+t2)

str_add('줄리엣')
str_add(t1='kevin')
str_add(t1='kevin ',t2='hate you')
str_add(t2='hate you',t1='kevin ')

#args, kwargs
def fun_1(*args):
    print(args)
#안에 인자를 출력하는 함수

fun_1('july','like salad')

# 인자 외에 dict타입으로 값을 받을 수 있다.
def fun_2(x,y,z,**kwargs):
    print(kwargs)
    print(x,y,z)
    
fun_2(10,9,8,a='홍길동',b='김개동',c='오길동')
