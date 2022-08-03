"""lambda는 이름없는 한줄짜리 함수"""
add_lam=lambda x,y:x+y
ret=add_lam(3,5)
print(ret)

"""033 마지막 예시를 람다로 해보자"""
new_dict={'Melon':'10$','Apple':'1$','iphone':'1200$'} 

def f1(x):
    return x[1] #인덱스 1인 요소 리턴 
ret1=sorted(new_dict)
ret1_items=sorted(new_dict.items())
#key= 자리에는 함수가 와야한다.

#함수 f1 대신에 람다
#ret2=sorted(new_dict.items(),key=f1)
ret2=sorted(new_dict.items(),key=lambda x:x[1])
print(ret2)