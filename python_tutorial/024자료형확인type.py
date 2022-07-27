from copyreg import dispatch_table


#어떤 변수가 있는데 그것이 어떤 타입인지 확인해보고 싶을 때 파이썬 내장함수인 type()이용해보자
num=10
li_st=[1,2,3]
s_tr='hellow'
dic_t={'a':1,'b':2}
def fun1():
    return 
print(type(num))
print(type(li_st))
print(type(s_tr))
print(type(dic_t))
print(type(fun1))