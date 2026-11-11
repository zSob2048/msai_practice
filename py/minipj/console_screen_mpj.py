from test.test import test_correct, test_score
from student.student import student


class console_sereen:
    
    def page_main_print():
        print(" 1) 학생 정보 등록")
        print(" 2) 시험 정보 입력")
        print(" -----------------")
        print(" 3) 학생 답안 입력")
        print(" -----------------")
        print(" 4) 시험 정답 출력")
        print(" 5) 성적      열람")
        print(" 5) 정답률    열람")
        print("...")
        print("10) 종료")
        return input("원하시는 업무 번호를 입력해주세요 : ")
    
####################################################################

    def page_1_print():
        print("-- 학생 정보 등록 --")
        s_name = input("이름 :")
        s_class = input("반   :")
        return student(None, s_name, s_class)
    
    def page_2_print():
        print("-- 시험 정보 입력 --")
        t_no = input("회차 :")
        q1 = input("1번 답   :")
        q2 = input("2번 답   :")
        q3 = input("3번 답   :")
        q4 = input("4번 답   :")
        q5 = input("5번 답   :")
        return test_correct(t_no, q1,q2,q3,q4,q5)
    
####################################################################

    def page_3_print():
        print("-- 학생 답안 입력 --")
        s_no = input("학번 :")
        t_no = input("회차 :")
        q1 = input("1번 답   :")
        q2 = input("2번 답   :")
        q3 = input("3번 답   :")
        q4 = input("4번 답   :")
        q5 = input("5번 답   :")
        return test_score(t_no,q1,q2 ,q3,q4,q5, s_no)
    
    
####################################################################

    def result_print(result):
        print(result)


####################################################################

## 개선해야할 점...
## 문항 수 하드코딩...
