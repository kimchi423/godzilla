# 주제: 예외처리 & 파일 입출력

# [예외처리]
# : 프로그램 실행 중에 발생하는 예외를 미연에 방지하는 것.

## 예외처리가 필요한 이유 예시:  계산기 프로그램
# num1 = float(input("소수점 넣어"))
# num2 = float(input("소수점 넣어"))
# andd = num1 + num2
# print(andd)
# try:
#     num1 = float(input("소수점 넣어"))
#     num2 = float(input("소수점 넣어"))
# except ValueError as e:
#     print("숫자만 넣으세요.")
# else:
#     andd = num1 + num2
#     print(andd)
# ## 예외처리 연습문제: 환율 계산 문제
# won = input("원화 금액 입력")
# dallor = input("달러 금액 입력")
#
# try:
#     print(int(won)/int(dallor))
# except ZeroDivisionError as e:
#     print("나누기 0은 불가능 합니다", e)
# except ValueError as e:
#     print("문자열 예외기 발생")
# else:
#     print("dpfj qkftod dksgka")
# finally:
#     print("예외가 발생하건 안하건 한다")
## 에러 발생시키기 연습문제


#
# st =input("입력하세요")
# if st == "fuck":
#     raise Exception("skQmsakf")
    # except skQmsakf
#
#
# # 예외처리 Mission: 영어단어 공부하기 문제를 'while문 + 예외 처리'로 풀어보자
#  wordlist = ["apple","banna","bababababababa"]
# # # print(wordlist[0])
# i=0
# # a = input()
# score = 0
# while True:
#     try:
#         user = input(wordlist[i]+"\n")
#     except:
#         break
#     if user == wordlist[1]:
#         score += 1
#     i += 1
# print(score)
# [파일 입출력]
# 파일 입출력 연습문제1: 파일 쓰기(w: 새로쓰기 혹은 덮어쓰기)
file = open('./fuck.txt','w',encoding="utf-8")
for i in range(1,11):
    file.write(f"{i}번째 줄입니다.\n")
file.close()
# 파일 입출력 연습문제2: 파일 추가하기(a: 추가하기)
# file = open('./fuck.txt','a',encoding="utf-8")
# for i in range(10,21):
#     file.write(f"{i}번째 줄입니다.\n")
# file.close()

# 파일 입출력 연습문제3: 파일 읽기(r: 읽기)
# way1) readline 함수 사용(한 줄 씩 읽어오기)
# file = open('./fuck.txt','r',encoding="utf-8")
# while True:
#     data = file.readline()
#     print(data)
#     if data == "":
#         break
# file.close()

# way2) readlines 함수 사용(모든 줄을 읽어와, 각 줄을 리스트의 요소로 반환)
# file = open('./fuck.txt','r',encoding="utf-8")
# data = file.readlines()
# print(data)
# for one in data:
#     print(one)
# file.close()
# way3) read 함수 사용(문서 전체를 하나의 문자열로 가져오기)
file = open('./fuck.txt','r',encoding="utf-8")
data = file.read()
print(data)