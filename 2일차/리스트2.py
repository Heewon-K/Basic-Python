words = ["school", "assembly", "chair", "hospital", "desk", "rain", "rainbow"]
print (f" original list = {words}")
print("데이터 개수 : ", len(words))

# 인덱싱
print(f"print one by using index = {words[0]}")

words[3] = "house"
print(f"changed the third word in the list => {words}")

# for문을 이용해 전부 출력
for w in words:
    print(w)

# 슬라이싱 - 파이썬 이후로 등장하는 문법   :   리스트변수[시작:종료:증감치]
print(f"slicing => {words[0:3]}") # 0,1,2 마지막(3)은 제외하고 출력

# 뒤에서부터 역순 출력 가능
print(f"reversed order => {words[6:3:-1]}")

# 완전히 역순으로
print(words[::-1]) #6, 5, 4, 3, 2, 1, 0

print(words[6:0:-1]) # 마지막 0번째는 출력이 되지 않는데 전체를 역순으로 출력하려면 [::-1]을 사용하자