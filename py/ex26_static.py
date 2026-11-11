# static
# 계산기!!

# 객체 왜 만드냐> 실생활스럽게 데이터 임시저장할때
# 변수 왜 만드냐> 데이터 임시저장할때

# static method ; 객체가 없어도 쓸 수 있는 메소드
#   일반 method ; 객체의 액션 > 객체가 있어야 사용 가능

class calculator:

    @staticmethod # 가독성 + 개발툴중에 없으면 에러띄우는 툴도 있음 (필수가 아니긴 함)
    def add_print(n1, n2): # 첫 파라메터로 self 빼기
        print(n1+n2)


calculator.add_print(10,30)

# static member veriable
    # static 으쩌고 저쩌고 > 중복되는 데이터를 여러번 저장 안하게 static 위치에>메모리 아끼기...
    # >>python은... 딱히 극적인 변화도없고 관심도 없음

