class C_Sum:
    def add(self,n1,n2):
        return n1+n2

class C_Sub(C_Sum):#C_sub는 C_Sum을 상속받았다.
    def sub(self,n1,n2):
        return n1-n2

obj=C_Sub()
print(obj.sub(7,4))
print(obj.add(7,4))#add를 호출해서 쓸 수 있는 이유는 상속을 받았기 때문이다

"""
상속을 하나의 부모클래스만 받는 것이 아니라 여러명의 부모 클래스를 받을 수 있습니다
class C_calculator(C_Sum,C_multiple,C_root,C_제곱)

자 그럼 계산기라는 클래스를 만들어서 곱셈 뺄셈 덧셈을 상속받으면 
계산기 기능을 갖춘 클래스를 만들 수 있겠습니다.
추가하고 싶은 기능을 가진 클래스를 만들어서 상속하게 하면 관리하기도 쉬울 것 같네요

"""
        