# Garbage Collection : heap 영역 자동 정리 시스템, python은 지원함
# 자동 발동 시점: 그 heap id를 가리키는 변수가 없게 되면

class std_:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("퇴학")

    def info_print(self):
        print("이름\t:", self.name)
        print("나이\t:", self.age)
        print("---")


s1 = std_("홍길동", 20)
s2 = std_("김길동", 22)
s3 = s1  # s1과 동명이인 s3

s1.info_print()
s2.info_print()
s3.info_print()

s1.name = "홍길도" # s1 개명
s1.info_print()
s3.info_print()

print(id(s1))
print(id(s2))
print(id(s3))
# >> s1과 s3 동일아이디 >> 이렇게 하면 안됨

s1 = None
print("풉킥")
s3 = None       # > 이시점에서 홍길도 사라짐
print("풉킥")
                # 프로그램 끝나면 김길동 집감

