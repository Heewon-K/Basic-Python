"""
홍길동, 90, 80, 70
장길산, 100, 100, 90
임꺽정, 80, 70, 60
list안에 dict로 넣고 총점, 평균 구해서 출력.
"""

scoreList = [
    {"name": "홍길동", "kor": 90, "eng":80, "math":70},
    {"name": "장길산", "kor": 100, "eng": 100, "math":90},
    {"name": "임꺽정", "kor": 80, "eng":70, "math":60}
]

for i in scoreList:
    i['total'] = i['kor'] + i['eng'] + i['math']
    i['avg'] = i['total'] / 3
    
for i in scoreList:
    print (f"{i['name']} {i['kor']}, {i['eng']}, {i['math']}, {i['total']}, {i['avg']}")