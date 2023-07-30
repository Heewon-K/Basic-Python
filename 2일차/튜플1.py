# 튜플 - 리스트와 사용법이 유사. 단, 읽기 전용 메모리! 값 수정이 안됨.
# 아무때나 대충 데이터를 묶어서 데리고 다닐깨, 리스트 타입보다 속다가 빠름
# 읽기 indexing지원, 슬라이싱도 지원. 내용은 못 바꿈

# [] - list, () - 튜플
fruits = ("사과", "배", "딸기", "포도")

print(fruits)
print (type(fruits)) # 타입출력
print(fruits[0])
print(fruits[0:3])
print(fruits[::-1])

"""
fruits[0] = "망고"      #에러 발생 => 튜플은 값 변경 불가
fruits.append('망고')   #추가 불가
fruits.remove('사과')   #삭제 불가
"""
for i in fruits:
    print(i)

# tuple 활용 예
name = "홍길동"
age = 12
phone = "010-0000-0000"
kor = 90

# str = 클라스. 파이썬이 제공하는 데이터 타입
# %s = 문자열, %d = 정수, %f = 실수
s1 = str.format("이름 : %s 나이 : %d 전화번호 : %s" % (name, age, phone))     # (name, age, phone)가 튜플
print(s1)

s1 = str.format("이름 : %s 국어 : %d 영어 : %d 수학 : %d" % ("임꺽정", 90, 80, 70))
print(s1)


# 변수 3개를 한번에 생성 => 이때 시스템 내부에서 튜플 사용!
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

# 두 변수의 값을 맞바꾸고자 한다
"""
a = 5           a = 7
          =>    
b = 7           b = 5

a=5
b=7
temp = a
a = b
b = temp
"""
a = 5
b = 7
a, b = b, a
print(f"a = {a}, b = {b}")

# 튜플은 주로 함수와 관련되서 사용된다!