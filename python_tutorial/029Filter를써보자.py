#파이썬 내장함수는 반복가능한 자료에서 특정조건을 만족하는 것만 골라낸다
# list에서 짝수만 골라보자

def pick_even(x):
    if x%2==0:
        return x
    
a_list=[1,2,3,4,5,6,7]
filter_list=filter(pick_even,a_list)
print(list(filter_list))