money = int(input("거스름돈 : "))
temp = money    # 원금액을 보존하려고 임시 변수 만들어서 값을 저장
unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in unit:
    if i > 10:
        m = temp // i
        print(f"{i} -> {m}장")
        temp = temp % i
    else:
        n = temp // i
        print(f"{i} -> {n}장")

# 선생님 방법
'''
# 화폐단위
money_unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# 화폐개수
money_cnt = [0, 0, 0, 0, 0, 0, 0, 0]

coins = 78760
temp = coins

money_cnt[0] = temp // money_unit[0]
temp = temp % money_unit[0]
print(money_cnt)

for i in range(0, len(money_unit)):
    money_cnt[i] = temp // money_unit[i]
    temp = temp % money_unit[i]

print(money_cnt)

# 거스름돈 입력: 78760
# 지폐 = 50000 1장
#       10000 2장
#       5000  1장
#       1000  3장
#       500   1개
#       100   2개
#       50    1개
#       10    1개
'''