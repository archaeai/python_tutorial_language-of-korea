"""
r,rt 텍스트 모드로 읽기
w,wt 텍스트 모드로 쓰기
a,at 텍스트 모드로 파일 마지막에 추가하기
rb 바이너리 모드로 읽기
wb 바이너리 모드로 쓰기
ab 바이너리 모드로 파일 마지막에 추가하기.
"""
#readlines() txt파일 내용 읽음
#readline() txt 
f1=open('data/text.txt','r')
strings = f1.readlines()
print(strings)