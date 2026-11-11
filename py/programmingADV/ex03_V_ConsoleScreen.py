from programmingADV.ex03_M_Company import Company


class ConsoleScreen:
    def info_input():
        name = input("이름:")
        add = input("주소:")
        ceo = input("사장:")
        emp = input("직원수:")
        return Company(name, add, ceo, emp)
    
    def result_print(result):
        print(result)