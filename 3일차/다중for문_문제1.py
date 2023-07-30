#     *     4/1
#    ***    3/3
#   *****   2/5
#  *******  1/7
# ********* 0/9
#  *******  1/7
#   *****

# 공백수 = line -i+1 
# 라인수     공백수      별 개수          라인수      공백수      별 개수
# 1          3           1               1           1           5   (4-1)*2 - 1
# 2          2           3               2           2           3   (4-2)*2 - 1
# 3          1           5               3           3           1   (4-3)*2 - 1
# 4          0           7                                           (Line - i)*2 - 1


# 삼각형
Line = 5
for i in range(0, Line):
    # 공백출력
    for j in range(0, Line - i):
        print(' ', end = '')
    # 별 그리기
    for k in range(0, 2*i-1):
        print('*', end = '')
    print()


# for i in range(1,15):
#     for j in range(14, i, -1):
#        print(" ", end = '')
#     for k in range(0, 2*i -1):
#         print("*", end = '')
#     print()
    

# 다이아몬드

Line = 5
for i in range(0, Line):
    # 공백출력
    for j in range(0, Line - i):
        print(' ', end = '')
    # 별 그리기
    for k in range(0, 2*i-1):
        print('*', end = '')
    print()
# 역순
for i in range(0, Line):
    for j in range(0, i):
        print(' ', end = '')
    for k in range(0, (Line-i)*2 - 1):
        print('*', end = '')
    print()
    
    
# for i in range(1,6):
#     for j in range(5, i, -1):
#        print(" ", end = '')
#     for k in range(0, 2*i -1):
#         print("*", end = '')
#     print()
    
# for i in range(5,1,-1):     # i = 5,4,3,2
#     for j in range():       #j = 1,2,3,4
#        print(" ", end = '')
#     for k in range(2*i-1, 0, -2):
#         print("*", end = '')
#     print()
