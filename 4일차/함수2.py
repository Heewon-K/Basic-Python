# 객체지향 언어의 특징이 오버로딩(함수의 이름은 같은데 다른 함수를 만들 수 있다)
# C언어  str -> int, int("1234") atoi(문자열을 정수), atof(문자열을 실수로)
# atoi(4) atoi(4.5) ------- 함수를 두개 만든다. 하나는 매개변수가 정수이고 하나는 매개변수 실수
# 문법을 버림, 안만든다

print(1)
print(3.4)
print("test")

# 매개변수에 기본값을 부여해서 호출 시에 새로운 값을 부여하는 방식에 따라 오버로딩과 유사한 효과를 가질 수 있다
def myadd(x,y,z):
    return x+y+z

print(myadd(10,20,30))

# 기본값: 매개변수를 선언하면서 값을 줄 수 있다. 기본값이라고 한다.
#         함수 호출시 매개변수에 값을 전달하지 않으면 기본값이 사용된다.
def myadd2(x=1,y=2,z=3):
    return x+y+z

print(myadd2())
print(myadd2(10))
print(myadd2(10,20))
print(myadd2(10,20,30))

print(myadd2(z=100))
