""" with는 무엇인가??
파이썬을 활용하다보면 파일을 열고 수정한 후 보통 Close( )와 같은 함수를 통해 파일을 닫는다. 
닫는 함수를 사용하지 않으면 프로그램이 종료되어도 계속 해당 객체가 열려있어 메모리를 점유하고 있게 된다. 
그래서 파이썬에서는 with ~ as ~ 라는 구문을 제공한다. 
개발자가 실수로 close( ) 를 하지 않아도 with ~ as ~ 구문이 끝나면 자동으로 객체를 close 하게 해준다. 
"""

with open('test4.txt','r') as f :
    text=f.read()
    print(text)
    pos=text.find('merry') # -1이면 없는 것   find는 최초로 발견되는 위치를 리턴한다. 
    print('안에 merry가 있을까요',pos)


"""
위에 것을 이용해서 빈도를 구해보자
"""
with open('test4.txt','r') as f :
    text=f.read().lower() #text.lower() #대소문자 상관없이 찾기 위해 소문자로 만든다음 검색
    count=0
    want_find='merry' #찾고싶은 단어
    pos=text.find(want_find)
    while pos != -1 :
        count+=1
        pos=text.find(want_find,pos+1)#찾은 위치 이후에서 다시 찾아보는 코드
    print('찾고자 하는 빈도수',count)
    
