# [시작:종료:증감치]
# range[시작,종료,증감치] - iterable : for 변수 in iterable객체:

for i in range(1,11):
    print(i)

print(range(1,11))
print(list(range(1,11)))

for i in range(1,11,2):
    print(i, end = ' ')
print()