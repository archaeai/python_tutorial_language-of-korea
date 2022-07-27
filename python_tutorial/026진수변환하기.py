#10진수를 16진수로
h1=hex(45)
h2=hex(40)
ret1=h1+h2
print(h1,' : ',ret1,' : ',type(h1)) # type이 str인 것을 알 수 있다.

a=int(h1,16)
b=int(h2,16)
ret2=a+b
print(a,' : ',ret2,' : ',type(a),' : ',hex(ret2))

#10진수를 2진수로
h1=bin(45)
h2=bin(40)
ret1=h1+h2
print(h1,' : ',ret1,' : ',type(h1)) # type이 str인 것을 알 수 있다.

a=int(h1,16)
b=int(h2,16)
ret2=a+b
print(a,' : ',ret2,' : ',type(a),' : ',bin(ret2))
