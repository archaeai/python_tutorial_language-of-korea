import time
print('1초간 정지')
time.sleep(1)

import new_package.new_lib 
#새로 만든 패키지에 있는 new_lib 모듈 임포트
#이렇게 하면 new_lib에 정의한 함수를 불러올 수가 있다.

ret1=new_package.new_lib.fun_add(3,4)
print(ret1)
ret2=new_package.new_lib.fun_txt_add('mallborow','dambae')
print(ret2)

