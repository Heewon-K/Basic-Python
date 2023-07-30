# list관련 문제
"""
1. flowers 변수에 다음 꽃들을 입력하세요.
작약, 국화, 목련, 목단, 장미, 해바라기

2. 0, 2, 4 번 데이터 출력하기 (인덱싱, 슬라이싱 둘 다 사용)

3. 해바라기 => 백일홍으로 수정

4 사루비아, 맨드라미 두 종류 추가하기

5. 목련 삭제

6. 현재 데이터 개수 출력

7. 마지막 데이터 삭제하기 
"""

flowers = ["작약", "국화", "목련", "목단", "장미", "해바라기"]
print(f"1번 문제 = {flowers}")

print(f"2번 문제 - 인덱싱 = {flowers[0], flowers[2], flowers[4]}")
print(f"2번 문제 - 슬라이싱 = {flowers[0:5:2]}")

flowers[5] = "백일홍"
print(f"3번 문제 = {flowers}")

flowers.append("사루비아")
flowers.append("맨드라미")
print(f"4번 문제 = {flowers}")

flowers.remove("목련")
print(f"5번 문제 = {flowers}")

print(f"6번 문제 = {len(flowers)}")

del flowers[len(flowers) - 1]
#del flowers[6]
print(f"7번 문제 = {flowers}")