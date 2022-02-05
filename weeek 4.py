# b = int(input("나이 입력 ㄱㄱ"))
# if b == 30:
#     print(f"")
# a = int(input("정수1 입력>>"))
# b = int(input("정수2 입력>>"))
# c = input("부호 입력>>")
# if c == "+":
#     print(a + b)
# elif c == "-":
#     print(a - b)
# elif c == "*":
#     print(a * b)
# elif c == "/":
#     print(a / b)
import random
import time

x = 1#random.randint(1,100)

while True:
    a = int(input("숫자 입력>>"))
    if a == x:
        time.sleep(1)
        b = int(input("진짜로? yes=1,no=2"))
        if b == 1:
            time.sleep(1)
            print("내가 졌네")
            time.sleep(1)
            print("정답")
            break
        elif b == 2:
            time.sleep(1)
            print("ㅋ")
            x = random.randint(1,100)
            time.sleep(1)

    elif a > x:
        # u = random.randint(1,2)
        # if u == 1:
        #     time.sleep(1)
        # elif u == 2:
        #     time.sleep(1)
        #     print("ㅋ")
        #     time.sleep(1)
        print("다운")
    elif a < x:
        # f = random.randint(1, 2)
        # if u == 1:
        #     time.sleep(1)
        # elif u == 2:
        #     time.sleep(1)
        #     print("ㅋ")
        #     time.sleep(1)
        print("업")

# 주제: 조건문

# [조건문]
## 조건문이란?: 조건에 따라 명령이 달라지는 제어문,
## 제어문 및 함수의 주요 특징!: 제어문에 포함된 문장은 "띄어쓰기"로 구분한다.
## if문: 조건의 시작. if에 걸린 조건이 참일 경우, 포함된 문장들 실행
## else문: 조건이 거짓(False)인 경우, 포함된 문장을 실행
## elif문: if문의 조건이 거짓인 경우 중에서 elif문의 조건이 참일 때, 포함된 문장 실행


# 연습문제: if 판단문과 if-else로 판단하는 프로그램


## mission1>> 구독자수를 입력받고 수익창출이 되는지 여부를 판단해보자
# a = int(input("구독자 수를 적으세요."))
# if a > 1000:
#     print("수익 가능")
# elif a < 1000:
#     print("수익 가능")
## mission2>> 현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력하는 프로그램
## 20000원 이상: 오늘 저녁은 치킨이닭!
## 10000원 이상: 이제는 고오급 음식인 떡볶이 ㅎㅎ
## 2000원 이상: 그래도 굶지는 않는 편의점 삼각김밥!
## 2000원 미만: 없다고 못먹는건 아니다. 친구에게 "한입만!"을 외쳐보자
# a = int(input("니 전재산"))
# if a > 20000:
#     print("치킨 enable")
# elif a > 10000:
#     print("떡 복이 enable")
# elif a > 5000:
#     print("삼각 enable")
# elif a < 5000:
#     print("gg")
## mission3>> 국어, 영어, 수학 점수를 입력받고 합계와 평균를 출력한 뒤.
## - 평균이 60점이 넘을 경우: "보충 대상자가 아닙니다. 즐거운 방학보내세요"
## - 퍙균이 60점이 넘지 않을 경우: "보충 대상자입니다. 당신의 방학은 이제 제껍니다 ㅎㅎ"
## 를 출력하는 프로그램을 만들어 보자
a = int(input("수학"))
b = int(input("국어"))
c = int(input("과학"))
d = int(input("영어"))
e = (a+b+c+d)/4
print(e)
if e < 60:
    print("당신의 방학은 이제 제껍니다 ㅎㅎ")
elif e > 60:
    print("보충 대상자가 아닙니다. 즐거운 방학보내세요")

