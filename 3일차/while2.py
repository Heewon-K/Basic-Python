# 정수를 입력받는다. 음수가 입력될 때까지 양의 정수나 0을 입력받아 합계와 평균을 구하자

i = int(input("정수를 입력하시오 : "))
count = 1
sum = 0
avg = 0
while i >= 0:
    sum = sum + i
    avg = sum / count
    count = count + 1
    i = int(input("정수를 입력하시오 : "))
# avg = sum / (count - 1)
print(f"합계 : {sum}, 평균 : {avg}")


# 선생님 방법
num = int(input("정수 : "))
nums = []
while num >= 0:
    nums.append(num)
    num = int(input("정수 : "))

print(nums)

sum = 0 
for i in range (0,len(nums)):
    sum = sum + nums[i]
    
print(f"합계 : {sum}, 평균 : {sum/len(nums)}")