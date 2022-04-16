# a = ["햄버거","치킨","피자"]
# b = input("메뉴 입력")
#
# c = int(input("수량"))
# if b == a[0]:
#     print(5000*c)


# altus w w w w w
# import random
#
# a = list(input("아이템 입력").split())
# b = random.choice(a)
# c = input("뽑힌 아이템은?")
# if b == c:
#     print("congraturation")
# else:
#     print(f"틀렸습니다 답은{b} 였습니다" )
import random

a = ["가위","바위","보"]
b = random.choice(a)
c = input("입력")
if c == b:
    print("비김")
elif (c == "바위" and b == "가위") or (c == "가위" and b == "보") or (c == "보" and b == "바위"):
    print("이김")
elif (c == "가위" and b == "바위") or (c == "보" and b == "가위") or (c == "바위" and b == "보"):
    print("짐")
