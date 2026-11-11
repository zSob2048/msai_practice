# 객체 지향 프로그래밍(Object-Oriented Programming) ; 프로그램 소스를 일상 언어스럽게 쓰자...
# <> 절차 지향 프로그래밍(Procedural Programming) ; 순서대로 잘 써서 프로그램 만들자...

# 개 이름이 후추(저장)
# 개 나이가 3살
# 그 개가 짖어...? : 멍 출력

## PP식
dog_name, dog_age = "후추", 3
print("%s(%d세) : 멍" % (dog_name, dog_age))

## OOP식
# 객체( : 실생활에 존재하는 어떤거)를 만드려면 클래스가 필요


# class : 객체 찍어낼때 쓰는 틀
class dog:
    # member variable; 객체의 속성
    name = None
    age = None

    # method : 객체의 액션, 프로그램상 필요한 기능 등..
    def bark(self):  # python에서는 변수 첫번째에 항상 self가 들어가야댐
        print("멍")
    def show_info(self):
        print(self.name)
        print(self.age)
# 다른 언어에선 클래스 명을 대문자로 시작하는 문화가 있음... (python은 ㄴㄴ >> 좀 헷갈려짐(class인지 method인지 그냥 ftn인지... ))

# object ( 혹은 instance ) : 찍어낸 그거
d = dog()  # 개를 하나 만들어서 d라는 변수에 할당
d.name = "후추"
d.age = 3
d.bark()
d.show_info()

print("---")

d2 = dog()  # 또 다른 개
d2.name = "라이터"
d2.age = 2
d2.bark()
d2.show_info()

# function vs method 비교
# fn: 기능 모아둔거
# m : 클래스에 들어가있는거

# 전역 변수 (global variable)               <> 지역 변수 (local variable)                                   <> 멤버 변수 (member variable)
# global 붙이면 어디서든 사용 가능한...     <> 함수나 method 속에서 만든 진행 동안만 사용하는... 바보문자    <> attribute, field 라고도 부름... class안의 변수(속성)

# 고양이 class


class cat:
    name = None  # "쪼찜이"라고 쓰면 전세계 모든 고양이 이름이 쪼찜이가됨
    age = None # 외부에서 추가 가능... 이렇게 잘 안씀
    def meow(self, cnt):
        print("냥"*cnt)
    def show_info(self):
        print(self.name)
        print(self.age)




c = cat()
print(c)  # >> <__main__.cat object at 0x0000025E2AAD00D0>
print(type(c))  # >> <class '__main__.cat'>

# 멤버변수 접근: 변수명.멤버변수명
c.name = "쪼찜이"
c.age = 1
c.weight = 3  # << 설정하지 않은 변수를 적으면... : python의 경우 외부에서 속성 추가 가능 but 다른언어에선... 
print(c.name)
print(c.age)
print(c.weight)

# 메소드 호출 : 원래 python 버전은:  클래스명.메소드명(지역변수)... 
# 다른 언어처럼 허용해준 버전... : 변수명.메소드명(지역변수)
cat.meow(c,2) # 원래는 이런식
c.meow(2) # 호출시 self는 제외
cat.show_info(c)
c.show_info()
