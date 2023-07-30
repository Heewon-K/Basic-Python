# 문제2. 이름, 국어, 영어, 수학을 입력받아 총점과 평균을 구한다.
# 이름 : 홍길동
# 국어 : 90
# 영어 : 80
# 수학 : 80
# 홍길동님의 총점은 250이고 평균은...

name = input("이름 = ")
x = int(input("국어점수 = "))
y = int(input("영어점수 = "))
z = int(input("수학점수 = "))

# fstring방식
print(f"{name}님의 총점은 {x+y+z}이고 평균은 {(x+y+z)/3}입니다.")



# 1. 입력 -> 2. 계산 -> 3. 출력
# 1. 입력
name = input("이름 = ")
x = int(input("국어점수 = "))
y = int(input("영어점수 = "))
z = int(input("수학점수 = "))

# 2. 계산
total = x + y + z
avg = total/3

# 3. 출력
print(f"{name}님의 총점은 {total}이고 평균은 {avg}입니다.")