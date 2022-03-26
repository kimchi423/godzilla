'''''
class cat:
    def __init__(self,name,age,jender):
        self.name = name
        self.age = age
        self.jender = jender



    def dry(self):
        print("야옹")
    def tail_wag(self):
        print("ㅑㅇ옹야옹")
    def susul(self):
        self.jender = "중성"
    def one_year(self):
        self.age += 1
    def info(self):
        print(f"고양이 이름은 {self.name}")
        print(f"나이는 {self.age}")
        print(f"성별은 {self.jender}")


dd = cat("김치",10,"남성")
aa = cat("김d치",10,"남성")
dd.info()
# aa.info()
# dd.susul()
# aa.susul()
# dd.info()
# aa.info()





af = input("a,b,c 중에서 고르세요")
af = dd.one_year
dd.info()

class car:
    def __init__(self,wheel = 2,kg = 100,maxspeed = 50,speed = 20):
        self.wheel = wheel
        self.kg = kg
        self.maxspeed = maxspeed
        self.speed = speed

    def light(self):
        print("번쩌번쩍")
        self.speed +=10

    def go_front(self):
        print("앞으로 가자")
        self.spped -= 10
    def ssssss(self):
        print(self.speed,self.wheel,self.kg,self.maxspeed)

truc = car(4,10000,180,50)
car1 = car(4,400,240,160)
super_car = car(4,100,340,280)
truc.ssssss()
car1.ssssss()
super_car.ssssss()
'''''

class monster:
    def __init__(self,name,attack,health,speed):
        self.name = name
        self.attack = attack
        self.health = health
        self.speed = speed
    def monster_print(self):
        print(f"[{self.name}]")
        print("ㄱㅣ본공격력:", self.attack)
        print("ㄱㅣ본cpfur:", self.health)
        print("ㄱㅣ본threh:", self.speed)
    def say(self):
        print("나는 개 무서운",self.name,"이다")
    def att(self):
        a = input("rhdrurgkf epalwl")
        self.health -= int(a)
    def rurn(self):
        print("지금",self.name,"의 체력은",self.health)

    def monster_print1(self):
        print(f"[{self.name}]")
        print("ㄱㅣ본공격력:", self.attack)
        print("ㄱㅣ본cpfur:", self.health)
        print("ㄱㅣ본threh:", self.speed)


wolf = monster("울프",100,100,50)
dragon = monster("드래곤",100000000000000000000000000000000000000000000000000000000,100000,5000000000000000000000000000000000000000000000000000000)
wolf.monster_print()
dragon.monster_print()
wolf.say()
godzilla = monster("고질라",1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,100000000000000000000002435924879236181787839074897961782905748189787489327897487289745487234758973289653729754387523479879347973497)
godzilla.monster_print()
wolf.att()
wolf.rurn()
wolf.monster_print1()