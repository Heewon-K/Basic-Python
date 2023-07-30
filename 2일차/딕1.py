# dict 타입은 키와 값 쌍으로 데이터를 저장하는 타입.
# 키와 값 자체는 어떤 타입이든 상관없는데 보통 키의 경우에는 문자열을 많이 사용한다
# 해쉬 테이블, 딕셔너리

colours = {"red":"빨간색", "blue":"파란색", "green":"초록색", "black":"검정색"}
print(colours['red'])       # red, blue, black값 등을 '키'라고 하고 '키'를 통해 데이터를 접근한다
print(colours['blue'])      # 인덱싱, 슬라이싱 적용 안됨.
print(colours['green'])
print(colours['black'])

# 추가/수정
# 키 값이 이미 존재했다면 수정, 값 바꿔치기, 없었으면 추가
colours['pink'] = "분홍색"  # 추가
colours['black'] = "까만색" # 수정
print(colours)

# 삭제
del colours['red']
print(colours)

# 키 값 목록 - 키 값 순서는 내부적으로 알아서 => 입력한 순서대로 나오지 않는다.
for key in colours:
    print(key, colours[key])

