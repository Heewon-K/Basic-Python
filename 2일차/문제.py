# 문제1. 3의 배수를 10개만 한줄로 출력
for i in range(3,31,3):
    print(i, end = ' ')
print()

# 문제2. 100, 90, 80, ..., 10까지 한줄로 출력
for i in range(100,0,-10):
    print(i, end = " ")
print()

# 문제3. 다음 리스트에서 홀수번째 방 데이터만 출력하기. 예) 1,3,5,7...번째
colours = ["red", "blue", "cyan", "magenta", "black", "brown", "yellow", "green"]

for i in range(1,len(colours),2):
    print(colours[i])

# 문제4. 구구단 4단 출력하기
dan = 4
for i in range(1,10):
    result = dan*i
    print(f"{dan} * {i} = {result}")

# 문제5. 정수를 1~100까지 출력하는데, 10개마다 줄바꿈을 할것. 힌트) if문 사용
# 방법 1
for i in range(1,101):
    list_ = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    if i in list_:
        print(i)
    else:
        print(i, end =' ')
        
# 방법 2
for i in range(1,101):
    if i % 10 == 0:
        print(i)
    else:
        print(i, end =' ')
        
# 선생님 방법
for i in range(1,101):
    print (i, end = ' ')
    if i % 10 == 0:
        print()
print()