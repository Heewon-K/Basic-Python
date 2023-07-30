# 문제 1: 정수를 음수가 입력 될 때까지 입력을 받아서 
# 각각 짝수와 홀수를 구분해서 짝수의 합계와 홀수의 합계를 출력

i = int(input("정수를 입력하시오 : "))
sum_o = 0
sum_e = 0

while i >= 0:
    if i % 2 == 0:
        sum_e = sum_e + i
    else:
        sum_o = sum_o + i
    i = int(input("정수를 입력하시오 : "))
print("짝수의 총합은 : ", sum_e)
print("홀수의 총합은 : ", sum_o)


# 평균도 구해보자
i = int(input("정수를 입력하시오 : "))
sum_o = 0
cnt_e = 0
sum_e = 0
cnt_o = 0
while i >= 0:
    if i % 2 == 0:
        sum_e = sum_e + i
        cnt_e = cnt_e + 1
    else:
        sum_o = sum_o + i
        cnt_o = cnt_o + 1
    i = int(input("정수를 입력하시오 : "))
print("짝수의 총합은 : ", sum_e, "짝수의 평균은 : ", sum_e/cnt_e)
print("홀수의 총합은 : ", sum_o, "홀수의 평균은 : ", sum_o/cnt_o)

# 문제 2:  정수를 음수가 입력 될 때까지 입력을 받아서 
# 각각 짝수와 홀수를 구분해서 분리시켜서 다른 리스트에 담아서 한번에 출력
# 출력 예) [2,4,8, ]
#          [3,7,9,15, ]

i = int(input("정수를 입력하시오 : "))
even_n = []
odd_n = []
while i >= 0:
    if i % 2 == 0:
        even_n.append(i)
    else:
        odd_n.append(i)
    i = int(input("정수를 입력하시오 : "))

print("입력된 짝수 : ", even_n)
print("입력된 홀수 : ", odd_n)
