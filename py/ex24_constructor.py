# constructor ; 생성자
# > 객체가 만들어질 때 호출되는 메소드
# destructor ; 소멸자
# > 객체가 사라질 때 호출되는 메소드


# 핸드폰 모델명 번호 가격 정보출력
class phone:
    model = None
    num = None
    price = None

    def info_print(self):
        print("모델명\t:%s" % self.model)
        print("번호\t:%s" % self.num)
        print("가격\t:%d만원" % self.price)

    # 기본 생성자 : 생성자 작업을 하지 않을결우 python 내부에서 자체적으로 만들어줌(pass같은)
    def __init__(self):  # 생성자
        print("핸드폰 생성")


p = phone()  # > 이 시점에 생성자 호출
p.model = "G S23 FE"
p.num = "010-1234-5678"
p.price = 32
p.info_print()

print("---")


# 콤퓨타 cpu ram hdd 출력
class PC:
    cpu = None
    ram = None
    hdd = None

    def info_print(self):
        print("CPU\t:", self.cpu)
        print("RAM\t:", self.ram)
        print("HDD\t:", self.hdd)

    def __init__(self, cpu, ram, hdd):  # 만들면서 cpu/ram/hdd 값 넣게...
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        print("콤퓨타 생성")


c = PC("i7-1234", 16, 250)  # >> 만들면서 정보 바로 기입...
c.info_print()

print("---")


# 펜... 이름 색 가격
class pen:
    # # python의 경우 여기 변수 잘 안씀(의미가 없어서...) >> Python 개발자들 이 멤버변수를 생성자에서 결정하는 문화가 잇음...
    # name = None
    # color = None
    # price = None

    def info_print(self):
        print("이름\t:", self.name)
        print("색상\t:", self.color)
        print("가격\t:", self.price)

    # def __init__(self, name, price):
    #     self.name = name
    #     self.price = price
    #     print("python의 경우 생성자 overloading 불가... 생성자는 1개만")

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        print("펜샀당")


pp = pen("모나미153", "검정", 500)
pp.info_print()

print("---")

# 책 제목 가격 
# 출력
class book:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print("책삿더")

    def __del__(self):
        print("책 팔았드")

    def info_print(self):
        print("이름\t:", self.name)
        print("가격\t:", self.price)

b = book("점프 투 파이썬", 20000)
b.info_print()