"""
iterable객체: list, tuple, range, filter, map, ...
for 변수 in iterable객체:
    문장
"""
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

# range(시작값, 종료값, 증감치)
print(range(1,11))      # "range(1,11)"이 나옴.

for i in range(1,11):   #1~10
    print(i)
    
# 짝수만 10개
for i in range (2,21,2):    #2,4,6,...
    print(i)

# 홀수만 10개
for i in range (1,20,2):    #1,3,5, ...
    print(i)
    
# print 옆으로 출력
print("이러면", end = ' ')
print("옆에 나와야한다")

print("1~10을 한줄로 출력")
for i in range(1,11):
    print(i, end = " ")
print()     # 이때 줄바꿈을 한다

for i in range(2,21,2):
    print(i, end = " ")
print()     # 이때 줄바꿈을 한다
for i in range(1,20,2):
    print(i, end = " ")
print()     # 이때 줄바꿈을 한다