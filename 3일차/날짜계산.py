"""
연도 월 일을 입력 받아서 그날이 그 해의 몇번째 날인지 맞추기
유년 4의 배수가 되면서 100의 배수가 되면 안되고 400의 배수는 윤년이다.
윤년의 경우, 2월이 29일 이 된다. 윤년이 아니면 28일.
"""


'''
< and, or, not : 논리연산자. 결과는 True/False >
- 조건식 1 and 조건식 2 : 두개의 조건이 둘 다 True일때, Ture.
- 조건식 1 or 조건식 2 : 두개의 조건 중 하나라도 True일때, Ture.
- not 조건식 : True -> False로 False -> True
- 우선 순위 : not -> and -> or
'''

# 윤년 계산
year = int(input("연도 : "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")
    

# 연도, 월, 일을 입력 받아서 그 날이 그 해의 몇번째 날인지 맞추기
year = int(input("연도 : "))
month = int(input("월 : "))
day =  int(input("일 : "))
m_days = [31,28,31,30,31,30,31,31,30,31,30,31]
sum = 0

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    m_days[1] = 29
    if month == 1:
        days = day
    else:
        for i in range(0, month - 1):
            sum = m_days[i] + sum
            days = day + sum
    print(f"{year}년 {month}월 {day}일은 {days}일째 입니다.")
else:
    if month == 1:
        days = day
    else:
        for i in range(0, month - 1):
            sum = m_days[i] + sum
            days = day + sum
    print(f"{year}년 {month}월 {day}일은 {days}일째 입니다.")
    
    
    
# 선생님 방법
year = int(input("연도 : "))
month = int(input("월 : "))
day =  int(input("일 : "))
month_last = [31,28,31,30,31,30,31,31,30,31,30,31]
days = 0   

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    month_last[1] = 29

for i in range(0, month - 1):
    days = days + month_last[i]
    
days = days + day

print(f"{days}번")