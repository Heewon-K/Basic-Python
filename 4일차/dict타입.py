# 키와 값 쌍으로 정보를 저장한다

mydict = {"red":"빨간색", "green":"초록색"}
mydict["blue"] = "파란색"   # 추가 또는 수정, 키값이 있으면 수정으로 판단한다

# keys()함수는 키값들만 변환한다

if "red" in mydict.keys():
    print("red가 있다")
else:
    print("red가 없다")


print(mydict.keys())    # dict_keys(['red', 'green', 'blue'])

# print(mydict['yellow'])     # 키값이 없으면 예외를 발생시킨다

# 삭제
del mydict['red']
print(mydict.keys())
