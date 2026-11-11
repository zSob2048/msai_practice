# str
# python은 모든 데이터가 객체 >
s = "asdf" # >> str("asdf")에서 str 생략해준것...
print(s)
print(type(s)) # class가 출력되는것...
print(id(s))

# python에는 형변환같은건 사실 없음
ss = "10"
ss = int(ss) # >>그냥 새 class

aa = 10 # >> str?? (x) python으로 만든 변수의 자료형 = object

# 다형성(polymorphism) : (oop에서) 상위 자료형 변수에 하위 자료형 변수를 넣을 수 있는...
# int a = 10 (o)
# string a = "10" (o)
# int a = "10" (x)
# float a = 10 (o)
# Python의 경우 다형성을 많이 활용하게됨

s = "키 : %.1fcm" % 159.98 # print 아니어도 사용가능

s = 'ㅋ' # Python의 경우 "" 와 ''의 구분 x
# 타언어 > ''안에는 1글자만
s = """ㅋ   ㅋㅋ
보입니카
    프린트해보샘""" 
print(s)
# 보입니카
#     프린트해보샘
# 쓴 모양 그대로 출력됨

# 주석 > 기계어 번역때 제외
"""
    이렇게해두면요 ㅋㅋ
    주석대용으로쓸수있긴한데
    따지고보면 str객체만든거 >>메모리공간먹음이(근데 변수 없어서 바로 사라지긴 함)
"""

class dog:
    """
        개고요
    """
    def bark(self):
        """
        짖습니다
        """
        print("망...")

help(dog)
# Help on class dog in module __main__:

# class dog(builtins.object)
#  |  개고요
#  |
#  |  Methods defined here:
#  |
#  |  bark(self)
#  |      짖습니다
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
# -- More  --

