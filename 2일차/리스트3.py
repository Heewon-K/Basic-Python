# 리스트에 데이터를 추가, 수정, 삭제하기
names = ["홍길동", "을지문덕", "강감찬"]
print(f"original list = {names}")

# 추가하기 : 리스트명.append('추가할 데이터')
names.append("서희")
names.append("윤관")

print(f"추가하기 = {names}")

# 수정하기 : 리스트명[수정할 데이터의 인덱스] = '수정 값'
names[0] = "광개토대왕"
names[1] = "장수왕"
print(f"수정하기 = {names}")

# 삭제하기 : 리스트명.remove('삭제할 데이터')
names.remove("서희")    # 내용을 찾아서 해당 내용이 있으면 첫번째 데이터를 삭제한다.
names.remove("강감찬")

print(f"삭제하기 = {names}")

# 위치 삭제 - 특이하게 명령어 형식이 다름 : del 리스트명[삭제할 데이터의 인덱스]
del names[0]
print(f"위치삭제 = {names}")