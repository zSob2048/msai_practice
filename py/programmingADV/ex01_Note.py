# ADV
# 프로그래밍 패러다임
# PP(절차지향)
# OOP(객체지향) > AOP(Aspect Oriented Programming, 관점 지향) : 객체지향식 중 공통된 부분을 따로 정리... 어쩌고저쩌고 말도참길게한다...

################################

# MVCNote
# MVC패턴 : 한 파일은 한사람이... > 한 파일에는 한 분야의 내용만 ; 파일 나눠서 작업
# 한 파일에 Model / View / Controller 셋 중 하나의 역할만 

################################
# Model      > 비즈니스 로직 (실제 계산) > back-end (+고객)
class Calculator:
    def add(x,y):
        return int(x)+int(y)


################################
# View       > 실제로 보이는 입/출력창 > front-end... 요즘은 react(=python아님)
class ConsoleScreen:
    def input_variable():
        x = input("x : ")
        y = input("y : ")
        return x, y
    def print_result(z):
        print(z)


################################
# Controller > 흐름 제어(프로그램 전체 종합, 실행중추) > 상황 보고 MA 각각 소환, 프로그램진입점, PL급 back-end....

# from V import ConsoleScreen
# from M import Calculator


if __name__ == "__main__":
    x,y = ConsoleScreen.input_variable()
    z = Calculator.add(x,y)
    ConsoleScreen.print_result(z)

################################

# DAO / DTO, VO, Bean 패턴(MVC안에서...)
# DAO(Data Access Object) : DB관련 작업하는 M영역
# DTO(Data Transfer/Temp Object), VO(Value Object), Bean(이건 java유래)
#    : 데이터 전송/임시저장용

################################

# 어떤 DB작업을 하던 공통부분 존재> 뭐 정리해서 들고값... 라이브러리로 만드샘...