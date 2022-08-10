"""
리스트 컴프리헨션은 직관적으로 리스트를 생성하는 방법입니다. 
대괄호 내부에 for문과 if 문을 사용하여 반복하며 조건에 만족하는 것만 리스트로 생성할 수 있습니다.
일반 적인 for if 문이 아닌
리스트 컴프리헨션을 사용하는 큰 이유는 직관적이고,  속도가 빠릅니다."""
test_list=[i for i in range(10)]
test_list_10=[i*10 for i in range(10)]
print(test_list)
print(test_list_10)