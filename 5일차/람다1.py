# 람다(lambda):이름이 없는 함수이다. 잠깐 만들어서 쓰고 버리는 일회용 함수이다
#              함수중에 계속적으로 존재해야 하는 함수가 있고, 잠깐 쓰고 버리는 일회용 함수를 만들어 쓰자

# filter(함수, iterable객체): 함수, 변환값이 True 또는 False이다. 이 함수의 실행결과가 참이면, 그 데이터만 보내주고 False면 데이터 안 준다.
#                            특정 조건에 맞는 데이터를 추출하고자 한다.

nums = [1,2,3,33,4,6,23,26,17,19,21,8,19,27]

# 짝수만 필터링
evenList = []
for n in nums:
    if n%2 == 0:
        evenList.append(n)
print(evenList)


def myfilter(nums):
    evenList = []
    for n in nums:
        if n%2 == 0:
            evenList.append(n)
print(evenList)


# 함수를 함수의 매개변수로 전달
# 함수도 주소이다. 변수에 함수를 저장할 수 있다.
# 함수에 매개변수로 전달되는 함수는 콜백함수라고 부른다.
# 호출자나 내가 직접하는게 아니고 다른 함수 (또는 시스템이다.)
# 함수의 매개변수나 변환값의 결정자는 내가 아니다. 약속된 형태만 보내야한다.
def myfilter(compare,nums):
    evenList = []
    for n in nums:
        if compare(n):
            evenList.append(n)
    return evenList

def myCompare(x):
    return x%2 == 1

print(myfilter(myCompare, nums))


def add(x,y):
    return x+y
calc = add      # 함수의 주소를 변수에 저장이 가능
print(calc(4,5))
print(add(4,5))

# 프로그램중에 일부만 살짝 고칠 수 있다면 함수를 미리 만들어놓고 나머지는 사용자가 완성하도록
print(list(filter(myCompare, nums)))


# myCompare => 람다형식
# lambda x : x%2==0 , return 문 사용 못함, 한줄만
print(list(filter(lambda x : x%2==0, nums)))


wordList = ["school", "book", "bookstore", "desk", "hospitl", "survey", "assembly", "president", 
            "flower", "language", "python", "sky", "cloud", "phone", "house"]

# 단어 길이가 5개 이상인 단어만 추출해보자
print(len("school")>=5)

for item in filter(lambda w : len(w)>=5, wordList):
    print(item)

# 단어가 b로 시작하는 것만 추출해보자
for item in filter(lambda w : w[0]=="b" , wordList):
    print(item)

# b를 포함하고 있는
for item in filter(lambda w : "b" in w , wordList):
    print(item)