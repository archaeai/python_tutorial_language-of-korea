"""문장에 문자 빈도수를 구해보자"""

with open('test3.txt','r') as f:
    txt=f.read()
    f_dict={}
    for alpha in txt:
        if alpha in f_dict:
            f_dict[alpha] +=1

        else:
            f_dict[alpha]=1

    ret=sorted(f_dict.items())
    for key,value in ret:
        if key =='\n':
            continue # 문자가 \n이면 밑에 프린트 문으로 가지 않고 처음으로 돌아감

        print('%s의 빈도는 %d입니다'%(key,value))     