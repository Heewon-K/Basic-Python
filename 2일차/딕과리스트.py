# list안에 dict타입을 둔다 - 주급

# 데이터가 하나도 없는 list 만드는 방법 : 예시) payList = [] 또는 payList = list()
# 데이터를 지정해서 payList 리스트 만들기!
payList = [
    {"name":"홍길동", "work_time":40, "per_hour":30000},
    {"name":"임꺽정", "work_time":30, "per_hour":20000},
    {"name":"장길산", "work_time":50, "per_hour":40000},
    {"name":"홍경래", "work_time":20, "per_hour":10000},
    {"name":"이징옥", "work_time":10, "per_hour":30000}
]

# 데이터가 잘 들어있나 확인! - 리스트 인덱싱과 키 값을 이용한 딕셔너리 인덱싱 사용
print(payList[0]["name"])
print(payList[1]["name"])
print(payList[2]["name"])

print(payList[0]["work_time"])
print(payList[1]["work_time"])
print(payList[2]["work_time"])

for pay in payList:
    print(pay["name"], pay["work_time"], pay["per_hour"])
    
# 급여 구하기
for pay in payList:
    pay["pay"] = pay["work_time"] * pay["per_hour"]
    
# 다시 출력
for pay in payList:
    print(pay["name"], pay["work_time"], pay["per_hour"], pay["pay"])