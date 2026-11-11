# 객체관의 관계
# has a / is a

# 객체관의 관계
# Human has a dog
# dog has a human

# Human has a 이름str
# Human has a 나이int

# print(type(1))   # >> <class 'int'>
# >> 다른 PL : 기본형, 객체, ...
# >> Python : 사실은 그냥 전부 class...

from os import name


class human:
    def __init__(self, name, age, pet):
        self.name = name
        self.age = age
        self.pet = pet

    def info_print(self):
        print(self.name, self.age)
        self.pet.info_print()


class dog:
    def __init__(self, name, species, insect):
        self.name = name
        self.species = species
        self.insect = insect

    def info_print(self):
        print(self.name, self.species)
        self.insect.info_print()


class insect:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def info_print(self):
        print(self.name, self.size)


i = insect("벼룩이", 1)
i.info_print()

print("---")

d = dog("순대", "말티즈", i)
d.info_print()

print("---")

h = human("홍길동", 30, d)
h.info_print()

print("---")

# Taxi is a Car  ... . ... ... 상- 하위관계에 있는... 포함관계 >> 상속 
# class안에 할당된 멤버들이 상속됨 (속성이...)

class product:
    def __init__(self, name , price):
        self.name = name
        self.price = price

    def info_print(self):
        print(self.name, self.price)

class pen(product): # >> product로 부터 상속받는 pen
    pass
# 상위 / 부모 / super 클래스... <> 하위 / 자식 / ...클래스

p = pen("모나미",500)
p.info_print()

print("---")
    
# 대부분의 언어에서 생성자는 상속시켜주지않음...
# Python의 경우 생성자에서 변수 결정...<< Python의 경우 생성자도 상속

class milk(product):
    # def __init__(self, name, price):
    #     super().__init__(name, price) # vscode의 서비스 여기서 고치면 댐
    def __init__(self, name, price, exp): # >> 상속받은거 아니고 새로 만든거... > 그니카이건사실overriding은 아님... 같은함수도아니니까
        super().__init__(name, price)
        self.exp = exp

    def info_print(self):
        # return super().info_print() # vscode의 서비스 여기서 고치면 댐
        super().info_print()
        print(self.exp)
    # overriding : 상속받아온 메소드를 개조할때... 
    # overriding vs overloading ... 

m = milk("매일우유",3000, "25-11-15")
m.info_print()

print("---")

class shoes(product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def info_print(self):
        super().info_print()
        print(self.size)

s= shoes("조던123",150000,270)
s.info_print()

print("---")

class PC(product):
    def __init__(self, name, price, cpu, ram,hdd):
        super().__init__(name, price)
        self.cpu=cpu
        self.ram=ram
        self.hdd=hdd

    def info_print(self):
        super().info_print()
        print(self.cpu,self.ram,self.hdd)

class notebook(PC): # 다단상속
    def __init__(self, name, price, cpu, ram, hdd,mass):
        super().__init__(name, price, cpu, ram, hdd)
        self.mass = mass

    def info_print(self):
        super().info_print()
        print(self.mass)

c = PC("매직스테이션123", 2000000, "i7-1234", 32,500)
n = notebook("그램123", 2500000, "i7-5678", 32, 1000, 3)
c.info_print()
n.info_print()

class 객체명(object): # >> (object) 가 원래 있는데 생략(기본값임)
    pass


# 다중상속 > 보통은 안됨 Python은 됨

class avrngers:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info_print(self):
        print(self.name,self.age)

    def attack(self):
        print("공격")

class human:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def eat(self):
        print("냠")

    def info_print(self):
        print(self.name,self.address)
        
# 다중상속 상황에서 이름이 같은 경우... > 먼저 상속받은거 우선 > 어차피 따로 넣어야함
class ironman(avrngers, human):
    def __init__(self, name, age):
        super().__init__(name, age)

i = ironman("토니", 40)
i.attack()
i.info_print()