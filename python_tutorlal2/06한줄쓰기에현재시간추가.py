""" 채팅같은 것을 보면 시간이 나온다 어떻게 표기할까"""
from time import localtime, strftime

count=1
data=[]

print('내용없이 엔터를 누르면 종료 됩니다')
while True:
    text=input('%d 파일에 저장할 내용 입력'%count)
    if text=='':
        break
    time_stamp=strftime('%Y-%m-%d %X\t',localtime())
    data.append(time_stamp +'\t'+text+'\n')
    count+=1

f=open('test2.txt','w')
f.writelines(data)
f.close
