import random
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
gameList=[]

def gameStart():
    #1. 컴퓨터가 값을 갖고 있다
    computer = random.randint(1,3)
    print("computr : ", computer)
    person = int(input("1. 가위, 2. 바위, 3. 보"))
    winner = whoWin(computer, person)
    gameInfo ={"computer":computer, "person":person, "winner":winner}
    output(gameInfo)
    gameList.append(gameInfo)

def output(gameInfo):
    temp1 = ["", "가위", "바위", "보"]
    temp2 = ["", "컴퓨터 승", "사람 승", "무승부"]
    c = gameInfo['computer']
    p = gameInfo['person']
    w = gameInfo['winner']
    print(f"컴퓨터 : {temp1[c]}, 사람 : {temp1[p]}, 승부 : {temp2[w]}")

def whoWin(computer, person):
    if computer == person:
        return 3
    
    if computer == 1:
        if person == 2:
            return 2 # 사람 승
    else:
        return 1
    
    if computer == 2:
        if person == 3:
            return 2 # 사람 승
    else:
        return 1
    
    if computer == 3:
        if person == 1:
            return 2 # 사람 승
    else:
        return 1
    
    
gameStart()