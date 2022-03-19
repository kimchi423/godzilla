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
