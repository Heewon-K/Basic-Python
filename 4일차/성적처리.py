# 성적처리: 이름, 국어, 영어, 수학 입력받아서 총점하고 평균
#          수우미양가까지 (90,80,70,60,50)

scoreList = []    # 공유메모리, 모든 함수가 사용한다.

def init():
    scoreList.append({"name":'홍길동', "kor": 90, "eng": 80, "math": 70})
    scoreList.append({"name":'임꺽정', "kor": 80, "eng": 70, "math": 50})
    scoreList.append({"name":'장길산', "kor": 50, "eng": 70, "math": 40})

def append():       # 데이터 추가만 담당하자
    data = dict()
    data["name"] = input("이름 : ")
    data["kor"] = int(input("국어 : "))
    data["eng"] = int(input("영어 : "))
    data["math"] = int(input("수학 : "))
    scoreList.append(data)

def edit():
    while True:
        print("1. 이름")
        print("2. 국어")
        print("3. 영어")
        print("4. 수학")
        print("0. 종료")
        sel = input("선택 : ")
        if sel == "1":
            for i in range(len(scoreList)):
                if scoreList[i]['name'] == input("바꿀 이름 : "):
                    scoreList[i]['name'] = input("새 이름 : ")
        elif sel == "2":
             for i in range(len(scoreList)):
                if scoreList[i]['name'] == input("바꿀 이름 : "):
                    scoreList[i]['kor'] = input("새 국어 점수 : ")
        elif sel == "3":
            for i in range(len(scoreList)):
                if scoreList[i]['name'] == input("바꿀 이름 : "):
                    scoreList[i]['eng'] = input("새 영어 점수 : ")
        elif sel == "4":
           for i in range(len(scoreList)):
                if scoreList[i]['name'] == input("바꿀 이름 : "):
                    scoreList[i]['math'] = input("새 수학 점수 : ")
        else:
            return # 함수가 종료, while도 종료한다


def remove():
    for i in range(len(scoreList)):
        if scoreList[i]['name'] == input("삭제할 이름 : "):
            del scoreList[i]
        return


def process():
    # pass : 나중에 채워넣기 위해 일단 넣어두는 것
    for item in scoreList:
        # item이 dict타입이라 아무 키나 추가 가능
        item["sum"] = item['kor'] + item['eng'] + item['math']
        item["avg"] = item['sum']/3
        if item["avg"] >= 90:
            item["grade"] = "수"
        elif item["avg"] >= 80:
            item["grade"] = "우"
        elif item["avg"] >= 70:
            item["grade"] = "미"
        elif item["avg"] >= 60:
            item["grade"] = "양"
        else:
            item["grade"] = "가"
    output_score()

def output():
    for item in scoreList:
        print(f"{item['name']} {item['kor']} {item['eng']} {item['math']}")
        
def output_score():
    for item in scoreList:
        print(f"{item['name']}  {item['kor']} {item['eng']} {item['math']} {item['sum']} {item['avg']} {item['grade']}") 
        
def menuDisplay():
    print("1. 추가")
    print("2. 출력")
    print("3. 계산")
    print("4. 삭제")
    print("5. 수정")
    print("0. 종료")
        
def start():
    init()
    while True:
        menuDisplay()
        sel = input("선택 : ")
        if sel == "1":
            append()
        elif sel == "2":
            output()
        elif sel == "3":
            process()
        elif sel == "4":
            remove()
        elif sel == "5":
            edit()
        else:
            return # 함수가 종료, while도 종료한다

start()