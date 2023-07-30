# for문 안에 또 for문이 있다

"""
for i in range(1,6):        
    for j n range (1,6):    
        코드                
        
==> i = 1 일때, j = 1,2,3,4,5
    i = 2 일때, j = 1,2,3,4,5
    i = 3 일때, j = 1,2,3,4,5 ....
"""

for i in range(1,6):
    print("i = ", i, " j = ", end ='')
    for j in range(1,6):
        print(j, end = ' ')     # 옆으로 출력
    print()     # 줄바꿈
    
    
# 이중for문을 사용해서 도형을 만들 수 있다
for i in range(1,6):
    for j in range(1,6):
        print("*", end = '')
    print()
    

# 삼각형
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end = '')
    print()

# 다이아몬드
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end = '')
    print()
for i in range(6,1,-1):
    for j in range(i,1,-1):
        print("*", end = '')
    print()