# 변수가 배열형태로 저장될때 다 갖고 있더.
# list, tuple, str(문자열)

s1 = "아메리카노,에스프레소,카페라떼,카라멜마키아또"
print(s1[0])
print(s1[1])
print(s1[2])
print(s1[6], s1[7], s1[8], s1[9], s1[10])

# str, tuple  둘다 read only라 인덱싱을 통한 값 변경은 불가
# s1[0] = "어" # TypeError: 'str' object does not support item assignment

# 슬라이싱 [시작:종료:증감치]    시작과 종료에는 값을 생략할 경우, 처음부터 마지막까지 라는 의미가 있다.
print(s1[::2])    # 0,2,4,6....
print(s1[:5])     # 0~4까지 잘라내기
print(s1[6:11])
print(s1[::-1])   # 뒤에서부터 역순으로 출력

s2 = s1[6:11]
print(s2)

# 토큰분리 : split 함수는 변환값이 list타입, 문자열에서 특정문자 기준으로 잘라낸다
wordList = s1.split(",")
print(wordList)

# "연결할 문자".join(리스트 타입)
s2 = " ".join(wordList)
print(s2)

s2 = ",".join(wordList)
print(s2)

# 문자열은 한번 값이 정해지면 자체는 수정불가
s1 = "hello, python"
s1 = "H" + s1[1:]     # H, ello python 문자하고 합친 문자가 다시 s1에 전달
print(s1)

s1 = "hello, python"
s1 = s1[:7] + "P" + s1[8:]
print(s1)


colourList = ["red", "white", "green", "cyan", "magenta", "violet", "blue"]
print(colourList[0])
print(colourList[2])
print(colourList[4])
print(colourList[5])

print(colourList[:4])
print(colourList[4::-1])    # 4번부터 역순



# 문제: 각 첫글자만 대문자로 바꾸어서 출력하기
print("R" + colourList[0][1:])

for i in range(0,len(colourList)):
    a = colourList[i][0:1]
    print(a.upper() + colourList[i][1:])
    

print(chr(ord(colourList[0][0])-32), colourList[0][1:])
print(colourList[0][0].capitalize(), colourList[0][1:])
colourList2 = []
for colour in colourList:
    temp = colour[0].capitalize() + colour[1:]
    colourList2.append(temp)
print(colourList2)


# 데이터 추가 수정 삭제
colourList2.append("Black")     # 무조건 맨 뒤에
colourList2.insert(0, "Yellow") # 위치 지정이 가능
print(colourList2)

# 수정
colourList2[0] = "Yellow"
print(colourList2)

# 삭제
colourList2.remove("Red")
# 위치값으로 삭제
del colourList2[5]
print(colourList2)