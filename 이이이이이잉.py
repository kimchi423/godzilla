# money = int(input("지불할 금액"))
# drink = int(input("음료 금액"))
#
# change_money = money - drink
# print(f"거스름돈은 {change_money}원 입니다")
#
#
# change_1000 = change_money // 1000
# change_500 = change_money % 1000 // 500
# change_10000 = change_money % 500 // 100
#
#
#
# print(f"1000원 {change_1000}개")
# print(f"500원 {change_500}개")
# print(f"100원 {change_10000}개")

#
# redius = float(input("반지름"))
# area = 3.14*redius*redius
# around = 2*3.14*redius
# print(f"원의 둘레{around}, 원의 면적{area}")

# a = float(input("1"))
# b = float(input("2"))
# c = input("3")
#
# if c =="/":
#     print(a/b)
# if c == "-":
#     print(a - b)
# if c == "+":
#     print(a + b)
# if c == "*":
#     print(a * b)
# import random
#
# x = random.randint(1,100)
#
# while True:
#     a = int(input("숫자 입력>>"))
#     if a == x:
#        print("정답")
#        break
#     elif a > x:
#         print("다운")
#     elif a < x:
#         print("업")

# menu = ["햄버거","김치","파스타","콜라"]
# price = [8500,10000,5000,1500]
#
# order = input("dma")
# num = int(input("수"))
#
# if menu[0] == order:
#     money = price[0] * num
# elif menu[1] == order:
#         money = price[1] * num
# elif menu[2] == order:
#     money = price[2] * num
# elif menu[3] == order:
#     money = price[3] * num
#
# print(f"가격{money}원")

# for i in range(10):
#     print("gaaaa")



# print(list(range(10)))
# print(list(range(2,11,2)))
# print(list(range(10,-1,-1)))
#
# for char in "안녕하세요":
#     print(char)


# i = 0
# while i<5:
#     print("hi")
#     i = i + 1

# i = 1
# while i<4:
#     print(f"{i}꼬마")
#     i = i + 1
# print("인디언")
# for char in range(1,4):
#     print(f"{char}꼬마")
# q =1
# while q < 10:
#     print(q, end="")
#     q = q + 2
#     continue
# q =0
# while q < 10:
#     q = q + 1
#     if q % 2 == 0:
#         continue
#     print(q, end="")
a=int(input("입력"))
for i in range(1,11):
    i = i*a
    print(i)