names = ["홍길동", "임꺽정", "장길산"]
work_hours = [40, 30, 20]
per_hours = [20000, 15000, 30000]

pays = []       # 비어있는 리스트 생성. 연산을 해서 데이터를 추가해야 한다.

for i in range(0,3):        # range(시작,종료,증감) = 해당하는 일련의 값을 준다.
    pays.append(work_hours[i] * per_hours[i])

# 출력하기
for i in range (0,3):
    print(names[i], "의 급여는", pays[i], "입니다.")