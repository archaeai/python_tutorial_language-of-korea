num_int=1    # 10진수 일반 숫자
b_2jin=0b10  # 2진수 
o_8jan=0o10  # 8진수 
h_16jin=0x10 # 16진수
print(num_int,':',b_2jin,':',o_8jan,':',h_16jin)


#실수형 자료 참고할 하나
#e3은 10^3을 의미함  e-3은 10 ^ -3
float1=1.23e3
print(float1) 
float2=102e-3
print(float2) 


""" 
추가 팁 
list =[1,2,3,4,5] 이런식
안에 있는 
1 2 3 4 5 는
0 1 2 3 4 인덱스로 지정가능
그러므로 list[0]=1
만약 list[0]=3 이렇게 코드를 실행하면
list[0]의 값이 3으로 바뀜

tuple=(3,4,5,6,7)
list 대괄호 tuple은 소괄호임 
리스트랑 달리 소인배라 리스트 처럼 안에 내용 바꿀 수 없음


딕셔너리 타입
키와 벨류로 구분됨 
{key:value,key:value...}
dict={'a':1,'b':2}
dict['a']는 대응되는 value인 1의 값을 갖는다.
dict['c']=3 이런식으로 안에 값을 추가 할 수 있다.

"""
