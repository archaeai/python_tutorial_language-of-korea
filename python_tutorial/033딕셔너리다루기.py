"""딕셔너리 타입은 키와 벨류로 구성 {'key1':'value1','key2':'value2'....}"""
"""요소 추가해보기"""
key_list=['p','j','c']
value_list=['python','java','c언어']
test_dict={}
for i,k in enumerate(key_list): #인덱스랑 요소를 같이 출력하는 enumerate
    val=value_list[i]
    test_dict[k]=val
print('test_dict',test_dict)

"""딕셔너리 요소변경"""

test_dict['c']='D언어'
print('c에서 d로',test_dict)

"""특정요소 삭제 del"""
del test_dict['c']
print('c삭제한 딕셔너리',test_dict)
""" key 만 추출하기, value만 추출하기 """

print('key만',test_dict.keys())
print('value만',test_dict.values())

"""key,value 값을 리스트로 items"""
items=test_dict.items()
print('items,key,value리스트',items)

"""특정 key or value가 존재하는 지 확인"""

print('#######특정 key value 존재 확인#####')
new_dict={'Melon':'10$','Apple':'1$','iphone':'1200$'} 
if 'Apple' in new_dict: #키확인
    print('여기 있음')
else:
    print('여기 없음')

if '1200$' in new_dict.values():
    print('여기 있음')
else:
    print('여기 없음')

"""정렬 하기 sorted, sorted는 그냥이용하면 키값을 정렬한 리스트를 리턴한다"""
print('#####정렬하기#####')
def f1(x):
    return x[1] #인덱스 1인 요소 리턴 
ret1=sorted(new_dict)
ret1_items=sorted(new_dict.items())
#key= 자리에는 함수가 와야한다.
ret2=sorted(new_dict.items(),key=f1)

# 이런식으로 특정 키가 제일 앞에오게 정렬할 수 있다

print('일반정렬',ret1)
print('특정키가 앞에오게 정렬',ret2)

