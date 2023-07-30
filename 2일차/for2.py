# 1~n까지의 합개 구하기
# sum = 1 + 2 + 3 + ... + n

"""
f(n) = 1 + ... + n
     = f(n-1) + n

sum         i           sum
0           1           1
1           2           3
3           3           6
6           4           10

sum = 0
sum = 0 + i     #누적하기, i = 1~10까지

"""
sum = 0
for i in range(1,101):
    sum = sum + i
    #print(i, sum)
print(sum)



# 문제1. 1~100까지 중에서 홀수 총합
sum = 0
for i in range(1,101,2):
    sum = sum + i

print(sum)

# 문제2. 1~100까지 중에서 7의 배수의 갯수 세기
cnt = 0
for i in range(1,100):
    if i%7 == 0:
        cnt = cnt + 1
print(cnt)
