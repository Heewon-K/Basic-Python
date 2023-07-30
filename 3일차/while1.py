"""
while문은 몇번 반복할지 알 수 없을 경우에 사용한다.
while 조건식:  # 조건식의 결과가 True일때 반복
    문장 1
    
조건식이 True가 될만한 수식
while 조건식:
    처리
    처리
    ...
    조건식이 False가 될만한 수식
    
# 1~10까지 출력하기
i = 1
while i <= 10:
    print i
    i = i + 1     # 마지막에 조건식이 False가 되도록 하는 수식이 있어야한다.
    
* while문은 특징이 한번도 수행 안 될 가능성이 있다. *

"""

# ctrl + c = 종료
# i = 1
# while i <= 10:
#     print(i)

# 1~10까지 옆으로 출력
i = 1
while i <= 10:
    print(i, end = ' ')
    i = i + 1
print()

# 1~n 까지 더해간다. 합이 최초로 1000을 넘는 n을 찾고 싶다.
i = 0
sum = 0
while sum < 1000:
    i = i + 1
    sum = sum + i
    
print(i)

