'''
# ord("문자") -> 해당 문자에 대한 unicode를 변환한다
print(ord("A"))     #65
print(ord("B"))     #66
print(ord("C"))     #67
print(ord("a"))     #97
print(ord("b"))     #98

print(ord("0"))     #48
print(ord("1"))     #49
print(ord("2"))     #50

# ord의 반대 역할 - chr(숫자) => 문자
print(chr(65))      #A
print(chr(66))      #B
print(chr(67))      #C
'''

# 알파벳 대문자 출력 - for문 사용 => ABCDEFGHIJKLMNOPQRXTUVWYZ
alphabet = []
for i in range(0,26):
    alphabet.append(chr(65 + i))
print(alphabet)

# BCDEFGHIJKLMNOPQRXTUVWYZ'A' -> CDEFGHIJKLMNOPQRXTUVWYZA'B' -> ... -> ZABCDEFGHIJKLMNOPQRXTUVWY - for문 사용

for i in range(0,25):
    alphabet.remove(chr(65 + i))
    alphabet.append(chr(65 + i))
    print(i, alphabet)
print(alphabet)

# 선생님 방법
for i in range(0,26):
    k=i
    for j in range(0,26):
        print(chr(k+65), end = '')
        k = k + 1
        if k > 25:
            k = 0
    print()