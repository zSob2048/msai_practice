from ex02_M_bmi import dataaa

class screennn():
    def input_data_():
        name = input("이름\t: ")
        height = input("키\t: ")
        weight = (input("몸무게\t: "))
        return dataaa(name, height, weight)


    def print_bmiresult(data):
        print("BMI(kg/m²): %.2f" % data.bmi)
        print("%s씨는 %s" % (data.name, data.result))