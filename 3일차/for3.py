# list에 데이터를 담아두고 리스트에 있는 데이터의 합과 평균 구하기

nums = [1,2,7,11,23,4,5,8,9,12]

# 배열에 있는 데이터들의 합을 구하기. 1+2+7+... 누적이라고 부른다
sum = 0 # 누적을 받을 변수의 값을 0으로 놓는다.

# sum = sum + sum[0]  #0 + 1 = 1
# sum = sum + sum[1]  #1 + 2 = 3 ...

for i in nums:
    sum = sum + i
    print(i, sum)
print(sum)

sum = 0
for i in range(0, len(nums)):
    sum = sum + nums[i]
print("합계 : ", sum)