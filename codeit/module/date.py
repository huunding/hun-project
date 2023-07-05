    # 현재 시간과 날짜
today = datetime.datetime.now()
print(today)

# 출력값을 "요일, 월 일 연도"로 포매팅
print(today.strftime("%A, %B %dth %Y"))

# 특정 시간과 날짜
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)

# 두 datetime의 차이
print(today - pi_day)