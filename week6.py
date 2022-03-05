# x = 10
# y = 20
# z = y
# y = x
# x = z
#   `
# print(x,y)
# a = int(input("몇명"))
# b = a*1
# c = a*2
# d = a*4
# print(f"치킨의 수는 {b}")
# print(f"맥주의 수는 {c}")
# print(f"케익의 수는 {d}")
# sum = 0
# for x in range(1,12):
#     sum = sum + x
# print(sum)b
sum = 0
b = int(input("부터 더할까요?"))
a = int(input("부터 어디까지 더할까요?"))
for x in range(b,a+1):
    if x % 2 != 0:
        sum = sum + x
print(sum)
#for문은 횟수
#while은 그냥 무한 반복


