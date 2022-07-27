# slice는 009를 참고하자
str_a='abcdefghigk' 
#str_a=[1,2,3,4,5,6] 리스트로도  실행해보자
#홀수번째만 뽑아보자
str_odd=str_a[::2]
print(str_odd)
#문자열을 거꾸로 만들기
str_rev=str_a[::-1]
print(str_rev)
print(list(reversed(str_a)))#거꾸로 만들어서 한글자씩 리스트에 담아보기

"""
참고로 문자열 끼리는 덧셈이 가능하다. 덧셈을 하면 합쳐진다."""
str1='삶은'
str2='계란이다'
str3='bamm'
str_add=str1+str2
print(str_add)
str_add2=str1+' '+str2+str3*3
print(str_add2)


"""in을 이용해서 특정문자가 있는지 확인"""
str_in='abcdf'
if 'a' in str_in:
    print('여기있어요 a')

"""문자열 길이구하기 len()"""
str_len='asd'
list_len=[1,2,3]
print('str',len(str_len),'list_len',len(list_len))

""" 문자열이 알파벳인지 검사 isalpha(), 숫자인지 검사 isdigit() 둘중하나인지 검사 isalnum()"""
str_al='hellow'
str_nal='안녕1'
str_num='123'
print('str_al:',str_al.isalpha())
print('str_nal:',str_nal.isalpha())
print('str_num:',str_num.isdigit())

"""문자열에서 대소문자 변환하기 upper,lower"""
str_test='Is It Ture?'
str_upper=str_test.upper()
str_lower=str_test.lower()
print('대문자:',str_upper,' 소문자:',str_lower)

"""문자열 양쪽 공백제거 왼쪽 공백은 lstrip() 오른쪽은 rstrip() 양쪽은 strip()"""
str_test1=' 공백이 없으면 장가를 못가요 '
print(str_test1.lstrip())
print(str_test1.rstrip())
print(str_test1.strip())

"""문자를 숫자로 숫자를 문자로"""
num=12
num_str=str(12)
num_str_num=int(num_str)
print(type(num),type(num_str),type(num_str_num))

"""문자에 있는 특정요소 개수 세기 count()를 이용하여"""
str_test3='You are so beautiful aabbccc'
word_count=str_test3.count('a')
print('a의 개수',word_count)

"""문자열에서 특정 문자(열) 위치 찾기"""
word_find=str_test3.find('a')#최초로 나타내는 위치
word_find10=str_test3.find('a',10)#인덱스 10이후부터 a위치
print('최초 a의 위치',word_find) 
print('두번째 a의 위치',word_find10)

"""***** 문자열을 특정문자로 분리하기 split"""
url='https:www.test.python/pandas/folium/kevin'
ret1=url.split('/') #split()안이 공백이라면 공백기준으로 split한다.
print(ret1)