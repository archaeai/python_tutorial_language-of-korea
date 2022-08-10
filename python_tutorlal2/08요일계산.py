from time import localtime


t=localtime() # 내 지역 지금 시간
print(t)#여기서 출력되는 값을 주목하자 
t_y=t.tm_year #  이런식으로 쓸수있다. str이라는 것을 참고하자


weekdays=['월','화','수','목','금','토','일']
week=weekdays[t.tm_wday] # wdays가 0이면 월 1이면 화 ... 6이면 일요일
print('오늘은 %s 데이데이'%week)
