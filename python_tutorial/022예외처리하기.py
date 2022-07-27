#오류가 발생했을때 오류 메시지를 보내거나 다른 것들을 시도하고싶다면?

try:
    print(obj)
except:
    print('obj가 정의되자않았습니다.')

#try 뒷부분을 실행하는데 obj를 정의하지 않았기때문에 오류가 나는 것이 당연합니다
#이럴때 ecept를 지정해 오류가 발생할 경우 어떻게 처리할지 결정합니다.


# try except else 구문 . try가 문제없이 실행되면 else가 실행된다.
try:
    print('문제없이 실행되었습니다')
except:
    print('obj가 정의되자않았습니다.')
else:
    print('문제가 없다는 것이 확인 되었습니다 main code를 실행합니다')


# try except finally 구문 . 오류이거나 아니거나 finally는 무조건 실행된다

try:
    print(obj)
    print('문제없이 실행되었습니다')
except:
    print('obj가 정의되자않았습니다.')
finally:
    print('나는 실행될거야')

# try except 구문에서 Execption as e code를 종종볼 수 있습니다. 파이썬은 몇몇 예외코드를
# execption 객체에 정의해두고 있습니다. 그 메시지를 예외상황에 호출해서 오류메시지를 확인해 보겠습니다.

"""
try:
    print(obj)
    print('문제없이 실행되었습니다')
except Exception as e:
    print(e)

import time
count=1
try:
    while True:
        print(count)
        count+=1
        time.sleep(0.5)
except KeyboardInterrupt:  # ctrl +c가 입력되면 발생하는 오류
    print('사용자에 의해 프로그램이 종료되었습니다')

"""