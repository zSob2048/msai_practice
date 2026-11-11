# ex14> OOD식 변경

class Doctor:
    def start(self):
        guest = self.call_guest()
        self.ask(guest)
        self.calculate(guest)
        self.tell_result(guest)
        # print(guest.name)
        

    def call_guest(self):
        return Guest()

    def ask(self, guest):
        guest.tell()

    def calculate(self, guest):
        if guest.height >10:
            guest.height /= 100
        guest.bmi = guest.weight / (guest.height) ** 2
        
        if guest.bmi >= 39:
            guest.result = "고도 비만"
        elif guest.bmi >= 32:
            guest.result = "중도 비만"
        elif guest.bmi >= 30:
            guest.result = "경도 비만"
        elif guest.bmi >= 24:
            guest.result = "과체중"
        elif guest.bmi >= 10:
            guest.result = "정상"

    def tell_result(self,guest):
        print("BMI(kg/m²): %.2f" % guest.bmi)
        print("%s씨는 %s" % (guest.name, guest.result))


class Guest:
    def tell(self):
        self.name = input("이름\t: ")
        self.height = float(input("키\t: "))
        self.weight = float(input("몸무게\t: "))

d = Doctor()
d.start()


# class Patient:
#     def __init__(self, name, hight, mass):
#         self.name = name
#         self.hight = hight
#         self.mass = mass

#     def bmi_print(self):
#         bmi_ = self.mass / (self.hight / 100) ** 2
#         print("BMI(kg/m²): %.2f" % bmi_)
#         result_ = "저체중"
#         if bmi_ >= 39:
#             result_ = "고도 비만"
#         elif bmi_ >= 32:
#             result_ = "중도 비만"
#         elif bmi_ >= 30:
#             result_ = "경도 비만"
#         elif bmi_ >= 24:
#             result_ = "과체중"
#         elif bmi_ >= 10:
#             result_ = "정상"
#         print("%s씨는 %s" % (self.name, result_))

# d = Doctor()
# d.start()
# p1 = Patient("냐", 160, 40)
# p1.bmi_print()


# 대 After COVID-19 시대를 맞이해 그냥 네이버 bmi검색기 돌린걸로 칩시다
# 의사는 없고 여러분은 죄다 통속의 뇌 입니다
