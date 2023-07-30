# pg.214

# 2번
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number > 100:
        print("-100 이상의 수:", number)
        

# 3번
# 1)
print("1)")
for number in numbers:
    if number % 2 == 0: # even number
        print(number, "는 짝수 입니다.")
    else:
        print(number, "는 홀수 입니다.")
  
# 2)        
print("2)")
for number in numbers:
    if number // 100 > 0:
        print(number, "는 3 자릿수 입니다.")
    elif 9 > number // 10 > 0:
        print(number, "는 2 자릿수 입니다.")
    else:
        print(number, "는 1 자릿수 입니다.")
        