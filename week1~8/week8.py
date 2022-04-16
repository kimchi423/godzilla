numbers1 = (1,1,1,1)
numbers2 = 1,1,1,1,

num1 = (1)         # ()로 만든 경우
num2 = (1,)         # (,)로 만든 경우
num3 = 1         # 숫자 1개만 넣어준 경우
num4 = 1,         # 숫자, 로 만들어준 경우
print("num1: ", num1, type(num1))
print("num2: ", num2, type(num2))
print("num3: ", num3, type(num3))
print("num4: ", num4, type(num4))

a = "딸기"
b = "맛있다"

print(f"{a}를 조조조좆도조존퓨엊ㄷㄹㄷ궈래우")
print("%s 먹고싶다"%(a))


numbers = 1,2,3,4,5,6,7,8,9
numbers = list(numbers)                         # 튜플을 list로 변환하기
print(numbers, type(numbers))
numbers = [1,2,3,4,5,6,7,8,9]                         # 다시 list를 tuple로 변환해주기
numbers = tuple(numbers)
print(numbers, type(numbers))

a = "100"
print(a,type(a))
a = int(a)
a = print(a,type(a))

a = 1,3,5,7,9
b = 2,4,6,8
numbers = a,b   # numbers로 a,b를 패킹해주기

c,d, = numbers

print(c,d,sep= "kimchi")

c,d=d,c









