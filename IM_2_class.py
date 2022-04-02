# 주제: class

# [클래스(class)]

# <class(1): 클래스 기본>
## 클래스와 객체
## 클래스: 객체를 만들기 위한 "설계도"
## 객체: 설계도로부터 만들어낸 "제품"

## 연습문제1: 클래스를 사용하는 이유
## LOL 인벤 챔피언들 정보: https://lol.inven.co.kr/dataninfo/champion/compare.php
## LOL 혹은 자신이 좋아하는 게임의 캐릭터 3가지를 선택하여 해당 캐릭터의 정보(채력, 공격력, 이동속도)를 입력하고,
## "게임 시작 인사, 캐릭터 능력을 각각 출력(함수)"등을 수행하는 프로그램을 만들어 보자

## ○ case1: class를 활용하지 않은 경우
# 정보 출력 함수 정의
'''''
# character_info() 함수 정의하기
def character_info(name, attack, health, speed):
    print(f"[{name}]") # name 출력
    print("ㄱㅣ본공격력:",attack)
    print("ㄱㅣ본cpfur:",health)
    print("ㄱㅣ본threh:",speed)



c1_name = "김치"
c1_health = 5333333333333333333333333333333333333375
c1_attack = 672349739287058923487942358907523478934258970234578942350789234589703458970234587902345897023458907234897234578909
c1_speed = 34352435643748659576734526345234356754869570876534652425436745
print(f"{c1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

c2_name = "qq"
c2_health = 575
c2_attack = 69
c2_speed = 345
print(f"{c2_name}님 소환사의 협곡에 오신 것을 환영합니다.")

c3_name = "ww"
c3_health = 575
c3_attack = 69
c3_speed = 345
print(f"{c3_name}님 소환사의 협곡에 오신 것을 환영합니다.")

c4_name = "ee"
c4_health = 575
c4_attack = 69
c4_speed = 345
print(f"{c4_name}님 소환사의 협곡에 오신 것을 환영합니다.")
character_info(c1_name,c1_attack,c1_health,c1_speed)
character_info(c2_name,c2_attack,c2_health,c2_speed)
character_info(c3_name,c3_attack,c3_health,c3_speed)
character_info(c4_name,c4_attack,c4_health,c4_speed)
'''''


'''''

    # name 출력
    # 기본 공격력(attack) 출력
    # 기본 체력(health) 출력
    # 기본 속도(speed) 출력

# character1 만들어주기(정보 할당)
    ## character1의 name 정의
    ## character1의 attack 정의
    ## character1의 health 정의
    ## character1의 speed 정의
print(f"{c1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

# <character_info()를 호출하여 character1의 정보 출력하기 >

# character2 만들어주기(정보 할당)
    ## character1의 name 정의
    ## character1의 attack 정의
    ## character1의 health 정의
    ## character1의 speed 정의
print(f"{character1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

character_info(character2_name, character2_attack, character2_health, character2_speed)
'''
## >> 캐릭터를 하나 만들 때마다 작성해야 하는 코드가 많고 복붙해서 수정하기도 귀찮다...
'''''

## ○ case2: class를 사용한 경우
# Character class 정의해주기
class Character:
    def __init__(self,name,attack,health,speed):
        self.name = name
        self.attack = attack
        self.health = health
        self.speed = speed
        print(f"{self.name}님 소환사의 협곡에 오신 것을 환영합니다.")

    # 생성자 정의 - name, attack, health, speed 입력
        # self.name
        # self.attack
        # self.healrh
        # self.speed
        # 소환사 협곡! 환영!

    # character_info() 메서드 정의
    def basic_info(self):
        print(f"[{self.name}]")
        print("ㄱㅣ본공격력:",self.attack)
        print("ㄱㅣ본cpfur:",self.health)
        print("ㄱㅣ본threh:",self.speed)
# name 출력
        # attack 출력
        # health 출력
        # speed 출력
gg = Character("레넥톤",69,858,8484834908234890)
# 첫번째 캐릭터 만들기
sdg = Character("레넥",609,8508,8484834908234890)
# 두번째 캐릭터 만들기
sdsd = Character("레",609,80508,8484834908234890)
# 첫번째 캐릭터의 character_info() 메서드 호출
# 두번째 캐릭터의 character_info() 메서드 호출
gg.basic_info()
'''
## <class 생성 및 호출>
## <class 생성 문법>
## class 클래스 이름:
##     def 메서드 이름1(self, 입력변수1, 입력변수2, ...):
##         실행명령
##     def 메서드 이름2(self, 입력변수1, 입력변수2. ...):
##         실행명령

## <class 호출 문법>
## 클래스 선언하기: 인스턴스 = 클래스이름()
## 매서드 호출하기: 인스턴스.메서드()

## 연습문제2: 모든 자료형은 class이다.
## 정수형, 실수형, 문자열, 불린형 등의 다양한 자료형을 가진 변수를 선언 후
## type() 명령을 통해 자료형을 출력하여 보자(class 확인 할 것)
## + 추가적으로 .__dir__() 역시 출력해보자
'''
a = 12              # int
b = 0.125           # float
c = '안녕하세요'      # str
d = True            # bool

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a.__dir__())
print(b.__dir__())
print(c.__dir__())
print(d.__dir__())
'''

## class(1) Mission
## : Mission에 언급된 내용대로 Cat class를 만들어 보자
'''
<Cat class 만들기!>
'''



# <class(2): 생성자와 상속>
## <생성자>
## : 객체가 생성될 때 자동으로 호출되는 메서드.
## [문법] class 클래스이름:
##           def __init__(self, 입력변수들):
##               초기화 실행 문장

## 생성자 연습문제
## : Monster 클래스를 만들고 step에 따라 생성자와 메서드가 추가된 Monster 클래스를 만들어보자.
## step1) 가장 기본적인 Monster 클래스를 만들어 보자
##        : say 메서드만을 가지는 Monster 클래스
'''
<Moster class 만들기>

<Monster 객체 생성 및 say 메서드 호출하기>
'''
## step2) Monster 클래스에 속성(name, health, attack, speed)을 추가하여 초기화해보자.
##        또한, 인스턴스 생성 시에 say의 내용이 출력되도록 만들어보자.
'''
<step1)에서의 Monster class 생성자의 속성 추가>

<goblin 객체 만들기(Monster 객체)>
'''

## step3) Monster 클래스에 메서드(decrease_health, get_health, info)를 추가한 후,
##        goblin과 wolf 객체를 생성하여 각 메서드들을 호출해보자.
'''
<Monster 객체에 여러가지 메서드 추가하기 >

<golblin과 wolf를 Monster 객체로 선언하고 메서드 호출하기>
'''

## <상속>
## : 부모 클래스의 속성과 메서드를 자식클래스가 물려받을 수 있도록 만든 기능
## 상속을 사용하는 이유: 클래스들에 중복된 코드를 제거하고 유지보수를 하기 위해 사용하기 위해서 사용.

## <메서드 오버라이딩(덮어쓰기)>
## : 부모 클래스에 있는 메서드를 자식클래스에서 동일한 이름으로 다시 만드는 것

## 상속 연습문제
## :Monster 클래스를 만들고, 상속을 활용하여 Wolf, Shark, Dragon 클래스를 만들어,각각의 객체를 생성해보자.
##
## step1) 부모 클래스: Monster 클래스 정의하기
## - 속성: name, health, attack
## - 메서드: move("self.name 지상에서 이동하기"를 출력하는 메서드, 이후 해당 몬스터의 이동방법이 출력되도록 할 것임.)

# <Monster class 작성하기>
class monster:
    def __init__(self,name,attack,health):
        self.name = name
        self.attack = attack
        self.health = health
    def move(self):
        print(f"[{self.name}]지상에서 이동하기")



## step2) 자식 클래스: Wolf, Shark, Dragon
## - Monster 클래스를 상속 받을 것.
## - 몬스터의 속성에 맞게 move를 메서드 오버라이딩할 것.
'''
<Moster class를 상속받은 Wolf, Shark, Dragon class 작성하기>

<각 class들로 객체 만든 후, move 메서드 호출하기>

class wolf(monster):
    pass

class shark(monster):
    def move(self):
        print(f"[{self.name}]해상에서 이동하기")
class dragon(monster):
    def move(self):
        print(f"[{self.name}]상공에서 이동하기")


wolf= wolf("울프",100,100)
shark = shark("tizm",100,100)
dragon = dragon("tiddzm",100,100)

wolf.move()
shark.move()
dragon.move()

'''





# <class(3): super()와 클래스 변수>
## super(): 부모클래스의 메서드들의 내용들을 그대로 가져와  자식 클래스 추가하고 싶은 경우에 사용하는 명령
## 클래스변수: 해당 클래스로 만든 모든 객체들이 공유하는 변수

## super()와 클래스 변수 연습문제: RPG게임 업데이트
## : ‘상속 및 메서드 오버라이딩 연습문제’에서 만들었던 내용들을 업데이트해보자
## - 드래곤 클래스에 ‘인스턴스 속성’으로 ‘3개의 스킬(불뿜기, 꼬리치기, 날개치기)’을 추가
## - 드래곤이 스킬을 쓰면 속성 중 하나가 무작위로 사용되도록 설정(random 모듈 이용)
'''
import random

class Monster:
    number = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.number -= 1
    def move(self):
        print(f"{self.name} 지상에서 이동하기")

class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):
        print(f"{self.name} 헤엄치기")

class Dragon(Monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ['불뿜기', '꼬리치기', '날개치기']
    def move(self):
        print(f"{self.name} 날기")
    def skill(self):
        print(f'스킬 {self.skills[random.randint(0,2)]}을(를) 사용했다.')

# 객체 생성 및 매서드 실행해보기
wolf = Wolf('늑대', 100, 50)
wolf.move()
print(wolf.number)

shark = Shark('아이상어', 500, 150)
shark.move()
print(shark.number)

dragon = Dragon('G-드래곤', 1000, 500)
dragon.move()
dragon.skill()
dragon.skill()
dragon.skill()
print(dragon.number)


## class Mission: 아이템 구성안과 설계도를 활용하여, class와 객체를 생성해 보자
## 이때, 부모 클래스: Item // 자식 클래스: WearableItem, UsableItem 이다.

'''
class item:
    item_num = 500
    def __init__(self,name,price,weight,work,drop):
        self.name = name
        self.price = price
        self.weight = weight
        self.work = work
        self.drop = drop
        self.item_num -= 1
    def displyitem(self):
        print(f"[{self.name}]")
        print(f"가격:{self.price}")
        print(f"무게:{self.weight}")
        print(f"설명:{self.work}")
    def sale(self):
        print(f"{self.name} 판매되었습니다. {self.price}가 지급됩니다")
    def drop(self):
        if self.drop == "T":
            print(f"{self.name}은 버릴 수 있는 아이템 입니다 ")
        else:
            print(f"{self.name}은 버릴 수 없는 아이템 입니다 ")

a = item("김치",10000000,100,"매운맛","T")
a.displyitem()
a.drop()