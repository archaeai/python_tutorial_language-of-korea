#16번을 as를 써서 improt 해보기
from new_package import new_lib as lib
ret1=lib.fun_add(3,4)
print(ret1)
ret2=lib.fun_txt_add('mallborow','dambae')
print(ret2)

"""
from 모듈 import 함수
from 패키지 import 모듈

"""