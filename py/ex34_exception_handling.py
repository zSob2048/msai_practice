# 예외 처리

# error     오류    > 실행 불가: 컴파일러방식에서
# warning   경고    > 실행은 되지만 문제 있는 코드
# exception 예외    > 개발자가 처리해야 하는 문제

# interpreter방식에서 에러랑 예외 구별하고 잡기 어려움 > 해당 부분 추후 확인

x = int(input("x:"))
y = int(input("y:"))
z = [124,123]

# print(x+y, x-y,x*y,x/y)

# 예외처리 
# try:
#   내용
# excpte 이름: 
#   대응

try:
    d = x/y
    print(d)
    print(z[y])

# except ZeroDivisionError:
#     print("ZeroDivisionError 처리")

# except IndexError:
#     print("IndexError 처리")
#     # 아무튼만이쓸수잇음

# except :
#     print("예외 처리")
#     # 하나로퉁쳐도됨

except Exception as aaaa:
    print(aaaa) # >> 이유가나옴
    print("내잘못아니고 니잘못임")

else: # try동안 문제 없는경우
    print("정상철이되었습니다")
finally: # try동안 문제발생과 관계 없이 >return보다 먼저< 실행
    print("end") 

##


class calculator:
    def input_variable(x,y):
        try: 
            z = x/y
            return z
        except:
            print("예외 발생")
            return -999
        finally:
            print("end")

##

# a = int("ㅋ") # >> ValueError
