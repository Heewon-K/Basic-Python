import random   # 외부 라이브러리를 불러온다. 자바의 import는 라이브러리 이름이 길어서 이름을 생략
# 파이썬의 import는 라이브러리를 메모리로 불러와서 결합한다

# print(random.randint(1,3))  # 1~3에 해당하는 랜덤값을 생성한다. 컴퓨터 내부의 시계를 이용한다.

# 리눅스 : 1933년 리누스 토발즈라는 대학생이 os를 만들면서 unix(서버용) => linux(pc용)
#           다른 사람들도 공부해라 소스공개
# 이전부터 소스공개를 주장하던 협회분들이 같이 하자 GNU협약
# 오픈 소스 - 파이썬 번역기 프로그램 소스를 공개한다
# 오픈소스가 무료인 경우가 많은거지 무료여야 하는건 아니다.
# 
# 하드웨어: os: 번역을 할때 OS에 특화
# 하드웨어: OS: 자바가상머신: 번역 자바가상머신이 알아듣게 실행할때 다시 OS가 알아듣는 말로
# GNU 협약을 따르는 경우 무조건 소스 공개를 해야 한다
# oracle, mysql, mysql(무료)

"""
가위바위보 게임
1. 가위
2. 바위
3. 보

1. 컴퓨터 값을 하나 랜덤하게 생성해서 갖는다. -> 리스트에 보관
2. 사람한테 입력 받는다 (1. 가위, 2. 바위, 3. 보) -> 리스트에 보관
3. 컴퓨터승, 사람승, 무승부 결정하고 -> 리스트에 보관
4. 출력

당신은 10게임을 했고 컴퓨터는 3승 당신은 2승 무승부는 2번이었다

"""
comp_list = []
human_list = []
win = 0
lost = 0
tie = 0
cnt = 0

def comp():
    input_c = random.randint(1,3)
    comp_list.append(input_c)
    
def hum():
    print("1. 가위", "2. 바위", "3. 보")
    input_h = int(input("선택 : "))
    human_list.append(input_h)
    
def process():
    global tie
    global lost
    global win
    for i in range(cnt):
        if comp_list[i] == human_list[i]:
            tie += 1
        else:
            if comp_list[i] == 1:   #가위
                if human_list[i] ==2:
                    win += 1
                else:
                    lost += 1
            if comp_list[i] == 2:   #바위
                if human_list[i] == 3:
                    win += 1
                else:
                    lost += 1
            if comp_list[i] == 3:   #보
                if human_list[i] ==1:
                    win += 1
                else:
                    lost += 1
    return
            
        
    #     if human_list[i] == 1:
    #         if comp_list[i] == 2:
    #             lost += 1
    
            
             

def result():
    print(comp_list)
    print(human_list)
    print(f"당신은 {cnt}게임을 했고 컴퓨터는 {lost}승 당신은 {win}승 무승부는 {tie}번이었다")

def menuDisplay():
    menus = ['1. play', '0. 종료']
    for menu in menus:
        print(menu)
    
def start():
    while True:
        menuDisplay()
        sel = int(input("선택 : "))
        if sel == 0:
            result()
            return # 함수종료
        else:
            global cnt
            cnt = cnt + 1
            hum()
            comp()
            process()



start()