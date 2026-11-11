from ex02_V_bmi import screennn
from ex02_M_bmi import calculate
# from ex02_M_bmi import dataaa

if __name__ == "__main__":
    data_guest = screennn.input_data_()
    calculate.bmi_calc(data_guest)
    screennn.print_bmiresult(data_guest)
