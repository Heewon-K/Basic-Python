# 구조적 프레임 방식
# 1. 추가
# 2. 수정
# 3. 삭제
# 4. 주급계산 및 출력
# 함수를 잘 만드는 방법(클린코드 - 자바): 1. 작게 만들어라 2. 더 작게 만들어라 3. 더 더 작게 만들어라
# 함수는 한가지의 기능에 집중하라. 
#   - 만약에 같이 진행되어야 하고 기능이 2가지면, 함수를 3개 만든다. 기능1 함수, 기능2 함수, 통합 함수를 만들어서 연결해라

payList = []    # 공유메모리, 모든 함수가 사용한다.

def init():
    payList.append({"name":'홍길동', "work_time":40, "per_hour":20000})
    payList.append({"name":'임꺽정', "work_time":30, "per_hour":20000})
    payList.append({"name":'장길산', "work_time":20, "per_hour":20000})

def append():       # 데이터 추가만 담당하자
    data = dict()
    data["name"] = input("이름 : ")
    data["work_time"] = int(input("일한 시간 : "))
    data["per_hour"] = int(input("시간당 단가 : "))
    payList.append(data)

def process():
    # pass : 나중에 채워넣기 위해 일단 넣어두는 것
    for item in payList:
        # item이 dict타입이라 아무 키나 추가 가능
        item["pay"] = item['work_time'] * item['per_hour']
    output_pay()

def output():
    for item in payList:
        print(f"{item['name']} {item['work_time']} {item['per_hour']}")
        
def output_pay():
    for item in payList:
        print(f"{item['name']} {item['work_time']} {item['per_hour']} {item['pay']}") 
        

# 위치를 찾는 함수인데 - 검색해서 출력, 수정, 삭제 시에도 사용
# 선형검색 => 람다, 컴프리핸션 (내일)
# 맨 처음 데이터부터 찾는 데이터가 나올때까지 차례대로 읽어본다 - 데이터가 없으면 None을 반환
def find(name):
    for i in range(0, len(payList)):
        if name == payList[i]['name']:
            return i    # 서로 일치하는 데이터가 있으면 위치를 반환하고 함수를 종료
    return None         # for문을 끝나도록 못 찾는 경우에는 없다는 의미로 None을 반환.
# 파이썬의 경우에는 함수에서 목적달성을 못 할 때 주로 None을 반환한다.

def search():
    name = input("찾을 이름 : ")
    pos = find(name)
    if pos == None:
        print(name + "을 찾지 못했습니다.")
        return      # 더 이상 수행을 하지 않는다. 이미 오류임. 여기서 else를 쓰지 않는게 프로그램의 확장성을 더 높여준다.
                    # if error: return 구조로 기술하면 함수를 보다 깔끔하고 확장성있게 만들 수 있다.
    # 에러가 아닐 때 처리
    item = payList[pos]     # 해당 위치 값을 가져와서 출력
    print(f"{item['name']} {item['work_time']} {item['per_hour']}")
     
     
def modify():
    name = input("수정할 이름 : ")
    pos = find(name)
    if pos == None:
        print(name + "을 찾지 못했습니다.")
        return
    # 에러가 아닐 때 처리
    data = payList[pos]     # 해당 위치 값을 가져와서 출력
    data["name"] = input("이름 : ")
    data["work_time"] = int(input("일한 시간 : "))
    data["per_hour"] = int(input("시간당 단가 : "))
    
     
def delete():
    name = input("수정할 이름 : ")
    pos = find(name)
    if pos == None:
        print(name + "을 찾지 못했습니다.")
        return
    del payList[pos]
     
def menuDisplay():
     print("1. 추가")
     print("2. 출력")
     print("3. 계산")
     print("4. 검색")
     print("5. 수정")
     print("6. 삭제")
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
            search()
        elif sel == "5":
            modify()
        elif sel == "6":
            delete()
        else:
            return # 함수가 종료, while도 종료한다

start()