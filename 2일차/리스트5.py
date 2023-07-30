# 검색(search) - 데이터가 있는 곳의 위치를 찾는 것
# 선형검색, 이분검색, 해쉬검색
# 시스템이 제공하는 검색을 사용

fruits = ["사과", "참외", "오렌지", "바나나", "사과", "딸기", "사과", "포도", "배"]

# 단어 in 리스트 - 해당 리스트에 단어가 존재하면 True, 없으면 False를 반환한다
print("사과" in fruits)     # '사과'라는 단어가 fruits안에 있느냐 없느냐; 있으면 True, 없으면 False
print("망고" in fruits)

print(fruits.index("사과"))      # 위치값을 반환
# print(fruits.index("망고"))    # 없으면 에러 발생, 혼자 사용 못함 -> in 연산자와 count 함수와 같이 사용

# count : 존재 갯수를 카운트한다
print(fruits.count("사과"))
print(fruits.count("망고"))
print(fruits.count("딸기"))
print(fruits.count("포도"))


# 조건식
# 망고가 있을때 없을때
"""
indentation - 파이썬은 들여쓰기, 내쓰기로 코드를 해석
if 조건식
    들여쓰기 반드시 필요. 내쓰기 하는 순간 if문과 관련없는 코드가 된다.
    탭키를 사용하기로 했으면 계속 탭키, 스페이스를 사용하기로 했으면 스페이스를 쓰자 
    * VSCode는 탭키 눌러도 스페이스 키로 바꾼다.
    
if 조건식: 조건식의 결과는 True 또는 False가 와야한다
    조건식이 참일때 처리 코드
else:
    조건식이 거짓일때 처리 코드
"""

if "망고" in fruits:
    print("망고의 위치 : ", function.index("망고"))
else:
    print("망고는 없습니다.")

if fruits.count("사과") > 0:
    print("사과의 위치 : ", fruits.index("사과"))
else:
    print("사과는 없습니다.")


