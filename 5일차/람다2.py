wordList = ["school", "book", "bookstore", "desk", "hospitl", "survey", "assembly", "president", 
            "flower", "language", "python", "sky", "cloud", "phone", "house"]

nums = [1,2,3,33,4,6,23,26,17,19,21,8,19,27]

# map : 연산을 수행해서 값을 변형해서 반환한다. x => x'
# nums에 값을 10씩 더하기
print(list(map(lambda x : x + 10, nums)))

# wordist의 문자들을 대문자로 변경
print(list(map(lambda x : x.upper(), wordList)))

# zip(list1,list2,list3) => 각 원소들끼리 결합해서 새로운 튜플로 만들어서 반환한다.
nameList = ["홍길동", "임꺽정" "장길산"]
phoneList = ["010-0000-0001", "010-0000-0002","010-0000-0003"]
emailList = ["1", "2", "3"]
for data in zip(nameList, phoneList, emailList):
    print(data, type(data))
    
# 정렬 - 하나는 자기자신의 수서 그대로, 바뀐순서만을 반환
#      - 자기자신의 순서를 바꾼다

# list타입에 존재하는 함수가 sort - 자기 자신의 순서를 바꾼다
# 특별히 말을 안하면 오름차순 정렬 - 작은 것 부터 큰거 순으로 늘어놓는 것을 오름차순
# 반대는 내림차순

# nums.sort()
# print(nums)

# nums.reverse()
# print(nums)

# wordList.sort()
# print(wordList)

# wordList.reverse()
# print(wordList)


sortedList = sorted(nums)
print("정렬 : ",sortedList)
print("원본 : ", nums)

sortedWord = sorted(wordList)
print("정렬 : ",sortedWord)
print("원본 : ", wordList)


dataList = [
    {"name":"강감찬", "age":23},
    {"name":"감강찬", "age":20},
    {"name":"김연경", "age":33},
    {"name":"조승연", "age":28},
    {"name":"김연아", "age":30},
    {"name":"이순신", "age":42},
    {"name":"서휘", "age":35},
    {"name":"윤관", "age":27},
    {"name":"박세리", "age":43}
]

# dataList -> 각 요소가 dict타입이다. x = dict타입이다
# dataList.sort(key = lambda x : x["name"])
# print(dataList)

# 이름을 역순으로 정렬(reserse = True)
sortedDataList = sorted(dataList, key = lambda x : x["name"], reverse = True)
print(sortedDataList)

# 나이순 정렬
sortedDataList_a = sorted(dataList, key = lambda x : x["age"])
print("나이순 :", sortedDataList_a)

# 나이순 역정렬
sortedDataList_a = sorted(dataList, key = lambda x : x["age"],  reverse = True)
print("나이 역순", sortedDataList_a)