# 문제 1: 주급계산하기. 근무시간 (30), 시간당급여액 (15000)
work_time = input("근무시간 = ")
per_hour = input("시간당급여액 = ")
pay = int(work_time) * int(per_hour)

print ("주급은", pay, "입니다")

# 파이썬의 경우, 문자열과 다른 타입을 + 연산 못함
# 형전환; 형을 바꾼다. int(): int로, str(): str로
print ("주급은" + str(pay) + "입니다")

# 문자열과 숫자를 섞어서 출력하고자 할때
# %d = decimal(숫자)
# 예전 버전 - 웹 프로그램, DB에 데이터 읽고 쓸 때,
print (str.format("주급은 %d 입니다" % pay))      
print(f"주급은{pay}입니다") # fstring 3.6부터 문자열 앞에 f를 쓴다.

