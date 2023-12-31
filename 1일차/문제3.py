#문제1. 미터를 입력받아 km와 m를 구하기
#입력 예) 미터 : 1234
#출력 예) 1234m는 1km와 234m입니다.

meter = int(input("미터 : "))
km = (meter // 1000)
m = (meter % 1000)
print(f"{meter}m는 {km}km와 {m}m입니다")


#문제2. 섭씨온도를 입력받아 화씨 온도 구하기
#공식: (섭씨 * 9/5) + 32 = 화씨

c = int(input("섭씨온도 = "))
f = c * 9 / 5 + 32
print(f"섭씨 {c}도는 화씨 {f}입니다")

#문제3. 식당에 다섯명이 가서 다음과 같은 주문을 하였다. 총 지불액은 얼마인가?
#다섯명이 같은 금액을 나누어서 지불한다고 할때 한명당 지불 금액은 얼마인가?
#주문내용 김치찌개 = 8000, 된장찌개 = 7000, 제육볶음 = 10000
# 입력방식   
# 김치찌개? 2
# 된장찌개? 1
# 제육볶음? 2

a = int(input("김치찌개? = "))
b = int(input("된장찌개? = "))
c = int(input("제육볶음? = "))

total = a * 8000 + b * 7000 + c * 10000
per_person = total/5

print(f"총 지불액은 {total}원이고 인당 지불액은 {per_person}원입니다.")