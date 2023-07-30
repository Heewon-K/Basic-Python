count = int(input("몇개? : "))
nums = []   # 데이터를 여러개 저장하려면 list()타입으로 만들어야한다. => nums = list()
for i in range(1, count + 1):
    n = int(input("숫자 : "))
    nums.append(n)
    
print(nums)