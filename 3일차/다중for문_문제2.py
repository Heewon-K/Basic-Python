# 문제:
# 1 2 3 4 5 6 7 8 9 10
# 11 12 13 ...... 20
# 1~100까지 한 줄에 열개씩, 이중for문 사용하기
    
    
for i in range(0,10):
    for j in range(1,11):
        print(i*10 + j, end = ' ')
    print()
  
  
# 선생님방법   
k = 1
for i in range(1,11):
    for j in range(1,11):
        print(k, end = '')
        k =k + 1
    print()

