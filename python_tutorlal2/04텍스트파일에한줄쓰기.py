count=1
data=[]

print('내용없이 엔터를 누르면 저장 됩니다')
while True:
    text=input('%d 파일에 저장할 내용 입력'%count)
    if text=='':
        break
    data.append(text+'\n')
    count+=1

    """
    open뒤에 나오는 알파벳에 대하여
"r"	Read를 뜻하며 파일을 수정하는 용도가 아니라 읽기 전용으로 엽니다. 파일이 없으면 에러가 발생합니다.
"w"	Write를 뜻하며 파일을 수정할때 사용하지만, 이미 파일에 내용이 있다면 새로 다시 씁니다. 파일이 존재하지 않으면 새로 생성합니다.
"a"	Append를 뜻하고 파일에 내용을 덧붙일때 사용하는 mode입니다. "w" 모드는 새롭게 덮어쓰는 것이고, "a" 모드는 뒤에 추가한다는 점이 다릅니다. 역시 파일이 존재하지 않으면 새롭게 생성합니다.
"x"	Create를 의미하며 파일을 생성합니다. 파일이 존재하면 에러를 반환합니다."""
f=open('test.txt','a')# w는 쓰기 모드라는 뜻
f.writelines(data)
f.close()

t=open('test.txt','r')
print(t.read())
t.close()

