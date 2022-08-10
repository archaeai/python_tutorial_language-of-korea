""" 텍스트 용량이 매우 큰 경우에 한번에 불러오는 것은 메모리 문제를 야기할 수 있다
그래서 한 줄씩 불러오도록 해보자"""
f=open('test.txt')
line_num=1
line=f.readline()
print(line_num,line)
line_num+=1 # line_num=line_num+1을 의미한다
line=f.readline()
print(line_num,line)
line_num+=1
line=f.readline()
print(line_num,line)


""" readline 말고 readlines()도 있는데 처음부터 끝까지 text파일을 읽어서
 각 줄을 요소로 가지는 리스트로 출력"""
lines=f.readlines()
print(lines,end='') # 출력값을 확인해보면 \n이 같이 나온다. 이것을 지워보자 
print([l.strip() for l in lines])  # strip()을 이용해 지웠다. 코드가 조금 낮설텐데
# 리스트 컴프리헨션을 검색해보자. 

f.close()