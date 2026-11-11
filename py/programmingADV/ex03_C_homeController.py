from programmingADV.ex03_M_CompanyDAO import CompanyDAO
from programmingADV.ex03_V_ConsoleScreen import ConsoleScreen


if __name__ == "__main__":
    c = ConsoleScreen.info_input()
    result = CompanyDAO.reg(c)
    ConsoleScreen.result_print(result)