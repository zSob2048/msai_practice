

from console_screen_mpj import console_sereen
from student.studentDAO import studentDAO
from test.test_correctDAO import test_correctDAO
from test.test_scoreDAO import test_scoreDAO



if __name__ == "__main__":
    studentDAO = studentDAO()
    test_correctDAO = test_correctDAO()
    test_scoreDAO = test_scoreDAO()

    while True:
        menu = console_sereen.page_main_print()
        if menu == "10":
            break

        elif menu == "1":
            student = console_sereen.page_1_print()
            result = studentDAO.reg(student)
            console_sereen.result_print(result)
            
        elif  menu == "2":
            test = console_sereen.page_2_print()
            result = test_correctDAO.reg(test)
            console_sereen.result_print(result)            

        elif menu == "3":
            score = console_sereen.page_3_print()
            result = test_scoreDAO.reg(score)
            console_sereen.result_print(result)