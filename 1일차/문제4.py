# 문제4. 동전 거스르기, 10만원
# 거스름돈 입력: 78760
# 지폐 = 50000 1장
#        10000 2장
#        5000  1장
#        1000  3장
#        500   1개
#        100   2개
#        50    1개
#        10    1개

change = int(input("거스름돈 : "))
num_50000 = change // 50000
num_10000 = (change - 50000*num_50000) // 10000
num_5000 = (change - 50000*num_50000 - 10000*num_10000) // 5000
num_1000 = (change - 50000*num_50000 - 10000*num_10000 - 5000*num_5000) // 1000
num_500 = (change - 50000*num_50000 - 10000*num_10000 - 5000*num_5000 - 1000*num_1000) // 500
num_100 = (change - 50000*num_50000 - 10000*num_10000 - 5000*num_5000 - 1000*num_1000 - 500*num_500) // 100
num_50 = (change - 50000*num_50000 - 10000*num_10000 - 5000*num_5000 - 1000*num_1000 - 500*num_500 - 100*num_100) // 50
num_10 = (change - 50000*num_50000 - 10000*num_10000 - 5000*num_5000 - 1000*num_1000 - 500*num_500 - 100*num_100 - 50*num_50) // 10

print(f"받아야할 거스름돈은 총 {change}원 => 50000원권 {num_50000}장, 10000원권 {num_10000}장, 5000원권 {num_5000}장, 1000원권 {num_1000}장, 500원 {num_500}개, 100원권 {num_100}개, 50원 {num_50}개, 10원 {num_10}개 입니다.")



# 다른 방법!
# cost = 거스름돈 -> 그 이후에 계속 cost = cost - ...으로 바꾸기
# print("50000" + "/t" + "str()" + "장") => str()사용, +를 사용하기 위해

# 선생님의 방법!
money = int(input("거스름돈 : "))
temp = money #원금액을 보존하려고 임시 변수 만들어서 값을 저장

m50000 = temp // 50000 
temp = temp % 50000

m10000 = temp // 10000
temp = temp % 10000

m5000 = temp // 5000
temp = temp % 5000

m1000 = temp // 1000
temp = temp % 1000

m500 = temp // 500
temp = temp % 500

m100 = temp // 100
temp = temp % 100

m50 = temp // 50
temp = temp % 50

m10 = temp // 10

print(f"50000 -> {m50000}장")
print(f"10000 -> {m10000}장")
print(f" 5000 -> {m5000}장")
print(f" 1000 -> {m1000}장")
print(f"  500 -> {m500}개")
print(f"  100 -> {m100}개")
print(f"   50 -> {m50}개")
print(f"   10 -> {m10}개")

