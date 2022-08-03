"""순차 적인 숫자가 있는 정수 리스트 만들기 range"""
int_list=list(range(10)) #0부터 9까지 그럼 1부터 10까지는 어떻게 할까 (range(1,11))
int_list1=list(range(10,20))#10부터 19까지 10개
print('range를 이용한 정수리스트',int_list,int_list1)
print('인덱스로 요소를 찍어볼 수 있다',int_list[0],int_list[3])

"""특정 요소의 위치 구하기 """
find_int=3
index_int=int_list.index(find_int)
print('3의 인덱스는 몇일까요',index_int)
"""리스트에 원하는 부분 값 변경하기"""
#인덱스가 3인 요소를 100으로 변경해보자
int_list[3]=100
print('list의 3번인덱스를 보자',int_list)

"""짝수번쨰만 뽑아보자"""
even_list=int_list[1::2] # 이 식의 뜻은 인덱스1(2번쨰)부터 2번쨰 것을 뽑는 것을 반복
print('짝수번째만 뽑은 list',even_list)
# 왜 인덱스가 1 3 5 7 9인 애들이 뽑혔을까?? 인덱스는 0부터 시작이다. 인덱스 1은 2번째 요소인것!!
odd_list=int_list[::2] # 짝수 식에서 1대신에 0이 생략되있는 것이다. 즉 처음부터 2번째 것을 뽑는 것을 반복
print('홀수번째만 뽑은 list',odd_list)

"""리스트요소를 역순으로 만드는 3가지 reverse() ,reversed() ,::-1"""

print('원본',int_list) 

reversed_list=reversed(int_list)
print('reveresed()',list(reversed_list))# 새로운 역방향 list 생성
print('::-1',int_list[::-1]) # 슬라이싱이용
int_list.reverse() #원본 변형
print('reverse()',int_list) #원본을 변형

""" 리스트를 합쳐보기 + """
#위에 만들었던 짝수 리스트와 홀수 리스트를 더해보겠습니다
add_list=even_list +odd_list
print('리스트 더하기',add_list) # 뒤에 있는 리스트가 뒤에 붙었습니다.
# 리스트를 반복하는 방법은 덧셈을 여러번 하는 겁니다.
# 같은 것 덧셈을 여러번하면 무엇일까요?(곱셈)


"""리스트에 요소 추가하기 append
아까는 몇번 인덱스에 있는 요소를 원하는 숫자로 바꿔봤다면 이번에는 추가를 해보겠습니다"""
#물론 리스트 하나를 만들어서 추가하고자 하는 리시트에 더하는 것도 가능합니다.
# 더할_리스트=[1,2,3]  
# 최종리스트=타겟리스트+ 더할리스트 이런식
test_list=[1,2,3,4]
test_list.append(100)
print('리스트에 요소추가',test_list)

"""내가 원하는 위치에 요소를 추가해보자. insert(원하는 인덱스,넣을 값)
내가 넣을 값이 원하는 인덱스에 들어가고 원래 그 인덱스에 요소는 뒤로 밀린다."""
test_list.insert(2,200)
print('원하는 위치에 추가한 리스트',test_list)

"""리스트 요소 제거하기 del (인덱스로 삭제) , remove(직접 입력해서 삭제)"""
del test_list[2]
print('2번인덱스 삭제한 list',test_list)

test_list.remove(100)
print('100을 삭제한 list',test_list)

"""리스트에서 특정 요소 개수 구하기 count"""
test_list.append(1) #1이 한개밖에 없으니 1개 추가 
print('리스트 내에 1과 2 개수를 세어보자',test_list.count(1),test_list.count(2))

"""리스트 요소 무작위로 섞기 shuffle() """
int_list=list(range(10))
print('섞기전 list',int_list)

from random import shuffle
shuffle(int_list)

print('섞은 후',int_list)

"""리스트 요소 정렬 sort  """
name_list=['Aimed','Gogumausi','Paker','Doby']

shuffle(name_list)
print('섞인 네임 리스트',name_list)
name_list.sort() #() 안에 reverse=True로 하면 역순으로 정렬된다

print('정렬된 네임리스트',name_list)

""" 리스트 요소 정렬하기 sorted"""
shuffle(name_list) #다시 섞기
ret1=sorted(name_list)
ret2=sorted(name_list,reverse=True)
print('섞은 것 sorted',name_list)
print('정렬한 sorted',ret1)
print('역정렬한 sorted',ret2)

"""인덱스랑 요소를 같이 추출해보기 enumerate()"""

for i,body in enumerate(ret1):
    print('순서 (%d)번 %s님 앞으로'%(i,body))

"""리스트에 모든 요소 더하기 sum ,숫자만 가능"""
list_int10=list(range(1,11))
print('1~10 list의 합',sum(list_int10))








