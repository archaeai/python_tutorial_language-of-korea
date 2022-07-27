#클래스 생성장 __init__에 대해서.
#클래스 인스턴스 객체가 생성될때. (밑에 코드에서 obj=MyClass()부분을 말함)
#자동으로 호출되는 메소드를 __init__인 클래스 생성자이다.
# 왜 생성자를 쓰는가?
#인스턴스의 생성과 초깃값 저장을 한 번에 할 수 있어서

class MyClass:
    def __init__(self):
        self.para='안녕'
        print('aaaaaaaaaaaa')

obj =MyClass()
print(obj.para)

#생성자에 인자가 있는 경우 
class MyClass1:
    def __init__(self,inja):
        self.val=inja
        self.para2='미튜'
        print('나이스투')
obj1=MyClass1('ninja') # 생성자에 필요한 인자가 있을 경우 객체를 생성할 때 인자를 넣어줘야한다
#obj1=MyClass1('ninja')
print(obj1.para2)
print(obj1.val)


"""
생성자를 사용하는 이유를 알려주는 예제 코드
class Dog:
    def __init__(self, legs, colour):
        self.legs = legs
        self.colour = colour

fido1 = Dog(4, "brown")
spot1 = Dog(3, "mostly yellow")
클래스 멤버로 선언하게 되면 클래스가 2개 필요하지만
생성자를 정의한다음 사용하면 쉽게 재활용할 수 있다.

"""

#소멸자  생성한 인스턴스 객체를 메모리에서 제거할 수있다.
class MyClass4:
    def __del__(self):
        print('객체가 제거되었습니다')

obj4=MyClass4()
del obj4

