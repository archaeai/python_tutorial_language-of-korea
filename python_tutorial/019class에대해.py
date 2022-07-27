#class는 프로그래머가 만든 하나의 독립공간이다. 클래스는 클래스 안에서 변수로 작용하는 
#밑에 str1같은 것들을 클래스 변수라고 부르고 fun_hi같은 것들을 class 메소드라고 한다.


class MyClass:
    str1='hi'
    def fun_hi(self):
        print(self.str1,'메소드에서 실행되는 인사')

my_cl=MyClass() #class 객체 생성
print(my_cl.str1,'나는 str1')
my_cl.fun_hi()

"""
클래스 멤버인 str1 호출은
my_cl.str1
클래스 메소드인 fun_hi 호출은
my_cl.fun_hi()
"""

"""
클래스는 또 하나의 공간 같은 느낌으로 독립된 공간이라고 생각하자.
클래스 멤버와 인스턴스 멤버
클래스 멤버는 클래스에 있는 전역변수고 
인스턴스 멤버는 클래스 메소드 안에 있는 지역변수다."""


class MyClass2:
    str2='hihey'
    def fun_hi_hey(self):
        test_text1='하이'
        print(self.str2) # 클래에 메소드 내에서 전역변수인 str2를 호출하려면 self.str2처럼 적어야한다.
        #print(str2)
        print(test_text1,'Class2에서 실행되는 문구')

my_cl2=MyClass2()
print(my_cl2.str2,'나는 str2')
my_cl2.fun_hi_hey()
print(MyClass2.str2,'클래스 밖에서 이런식으로도 쓸수 있는데 잘안씀')
#그냥 헷갈리니까 객체만들어서 씁시다

# 추가적인 Class method예시 
class MyClass3:
    def my_cl3(self):
        print('나는 my_cl')
    
    def my_cl4(self,boom):
        print("%s~~~~~~"%boom) # 복습! s는 문장 d는 정수 f는 실수

obj=MyClass3()
obj.my_cl3()
obj.my_cl4('bamm')