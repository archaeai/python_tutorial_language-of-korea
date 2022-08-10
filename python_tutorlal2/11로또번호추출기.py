from random import shuffle,randint
#1 리스트 컴프리헨션과 shuffle을 이용해보기
lotto_num_list=[x+1 for x in range(45)]
print(lotto_num_list)
shuffle(lotto_num_list)
print(lotto_num_list)

final_num=[]
for i in range(6):
    final_num.append(lotto_num_list[i])

print('로또번호',final_num)

#randint 로 해보기  randint(최대,최소) 범위에 있는 정수를 리턴
lotto_num2=[]
for j in range(6):
    lotto_num2.append(randint(1,45))
print('randint',lotto_num2)