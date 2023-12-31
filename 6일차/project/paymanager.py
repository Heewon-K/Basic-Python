from pay import Pay # from 파일명 import 클래스명 

class PayManager:
    payList = []
    def __init__(self):
        self.payList.append(Pay("A", 30, 20000))
        self.payList.append(Pay("B", 40, 30000))
        self.payList.append(Pay("C", 20, 10000))
        self.payList.append(Pay("D", 15, 20000))
        self.payList.append(Pay("E", 25, 30000))
        
    def append(self):
        pay = Pay()
        pay.name = input("이름 : ")
        pay.work_time = int(input("일한시간 : "))
        pay.per_pay = int(input("시간당 급여액  : "))
        pay.calculate()
        self.payList.append(pay)
                    
    def output(self):
        for pay in self.payList:
            pay.output()
    
    def menuDisplay(self):
        print("1. 추가")
        print("2. 출력")
        print("3. 검색")
        print("4. 수정")
        print("5. 삭제")
        print("6. 정렬")
        print("0. 종료")
        
        
    def start(self):
        while True: # 무한루프
            self.menuDisplay()
            sel = input("선택 : ")
            if sel=="1":
                self.append()
            elif sel=="2":
                self.output()
            else: 
                print("프로그램을 종료합니다")
                return 


# 하나의 파일에 하나의 클래스를 만든다
# 남의 파일에 있을때 모듈을 가져오려면 import를 사용한다 
# 외부 모듈 불러오기        

if __name__ == "__main__":
    mgr = PayManager()
    mgr.start()

