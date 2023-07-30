scoreList = [
    {"name":"홍길동", "kor":90, "eng": 80, "mat": 90},
    {"name":"둘리", "kor":100, "eng": 40, "mat": 90},
    {"name":"임꺽정", "kor":100, "eng": 100, "mat": 100},
    {"name":"장길산", "kor":70, "eng": 60, "mat": 70},
    {"name":"도우너", "kor":90, "eng": 80, "mat": 90}
]

# 총점, 평균, 학점
def process(score):
    score["total"] = score["kor"] + score["eng"] + score["mat"]
    score["avg"] = round(score["total"]/3, 2)
    score["grade"] = ""
    if score["avg"] >= 90:
        score["grade"] = '수'
    elif score["avg"] >= 80:
        score["grade"] = '우'
    elif score["avg"] >= 70:
        score["grade"] = '미'
    elif score["avg"] >= 60:
        score["grade"] = '양'
    else:
        score["grade"] = '가'
        
# 한명분만 출력
def output(s):
    print(f"{s['name']}", end = ' ')
    print(f"{s['kor']}", end = ' ')
    print(f"{s['eng']}", end = ' ')
    print(f"{s['mat']}", end = ' ')
    print(f"{s['total']}", end = ' ')
    print(f"{s['avg']}", end = ' ')
    print(f"{s['grade']}")
    
def processALL():
    for score in scoreList:
        process(score)

def outputALL():
    for score in scoreList:
        output(score)

# processALL()
# outputALL()



# 검색함수
def search():
    name = input("찾을 이름 : ")
    # result = list(filter(lambda x : x['name'] == name, scoreList))
    result = [x for x in scoreList if x['name'] == name]
    if len(result) == 0:
        print(f"{name}을/를 찾을 수 없습니다.")
        return
    
    for item in result:
        output(item)
    
# 수정
def modify():
    name = input("찾을 이름 : ")
    # result = list(filter(lambda x : x['name'] == name, scoreList))
    result = [x for x in scoreList if x['name'] == name]
    if len(result) == 0:
        print(f"{name}을/를 찾을 수 없습니다.")
        return
    
    result[0]["name"] = input("이름 : ")
    result[0]["kor"] = int(input("국어 : "))
    result[0]["eng"] = int(input("영어 : "))
    result[0]["mat"] = int(input("수학 : "))
    process(result[0])  #다시 계산하기
    
    
# 삭제
def delete():
    name = input("찾을 이름 : ")
    # result = list(filter(lambda x : x['name'] == name, scoreList))
    result = [x for x in scoreList if x['name'] == name]
    if len(result) == 0:
        print(f"{name}을/를 찾을 수 없습니다.")
        return
    scoreList.remove(result[0])
    processALL()  # 다시 계산하기
    

# 정렬
#   1. 이름
#   2. 총점
#   3. 국어성적
def sort_score():
    print("1. 이름", "2. 총점", "3. 국어")
    sel = input("선택 : ")
    if sel == "1":
        key = "name"
        reverse_k = False
        # sortedList = sorted(scoreList, key = lambda x : x["name"])
        # print(sortedList)
    elif sel == "2":
        key = "total"
        reverse_k = True
        # sortedList = sorted(scoreList, key = lambda x : x["total"])
        # print(sortedList)
    else:
        key = "kor"
        reverse_k = True
        # sortedList = sorted(scoreList, key = lambda x : x["kor"])
        # print(sortedList)
    sortedList = sorted(scoreList, key = lambda x : x[key], reverse= reverse_k )
    for s in sortedList:
        output(s)

def append():
    data = dict()
    data["name"] = input("이름 : ")
    data["kor"] = int(input("국어 : "))
    data["eng"] = int(input("영어 : "))
    data["mat"] = int(input("수학 : "))
    scoreList.append(data)
    processALL()


def menuDisplay():
    menus = ['1. 추가', '2. 출력', '3. 검색', '4. 수정','5. 삭제','6. 정렬','0. 종료']
    for menu in menus:
        print(menu)

# def start():
    # processALL()
    # while True:
    #     menuDisplay()
    #     sel = input("선택 : ")
    #     if sel == "1":
    #         append()
    #     elif sel == "2":
    #         outputALL()
    #     elif sel == "3":
    #         search()
    #     elif sel == "4":
    #         modify()
    #     elif sel == "5":
    #         delete()
    #     elif sel == "6":
    #         sort_score()
    #     else:
    #         print('프로그램을 종료합니다.')
    #         return #함수 종료

def start():
    functionList = [None, append, outputALL, search, modify, delete, sort_score]
    processALL()
    while True:
        menuDisplay()
        sel = int(input("선택 : "))
        if sel<1 or sel>len(functionList):
            print('프로그램을 종료합니다.')
            return #함수종료
        
        functionList[sel]()
    
start()