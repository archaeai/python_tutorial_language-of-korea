from datetime import datetime,timedelta


"""
얼마나 오래 만났는지 계산"""

now  = datetime.now()
print("현재 :", now)	
strat_love = datetime(2019, 3, 14,9,30,15)

how_long = now - strat_love
print('만난지',how_long,' 만큼 됐습니다')

"""
기념일 구하기
"""
days_100=strat_love + timedelta(days=100)
print(days_100.date(),'100일기념') #date()는 시간 분 초를 빼고 날짜만 나오게 해준다