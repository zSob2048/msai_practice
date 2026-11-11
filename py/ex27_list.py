# 2차원 list
import test


score = [["홍길동", 100, 90, 80], ["김길동", 10, 9, 80], ["최길동", 55, 11, 33]]

print(score[0])  # ["홍길동", 100, 90, 80]
print(score[0][0])  # "홍길동"
print(score[0][2])  # 90


class student:
    def __init__(self, name, kor, math, eng):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng

    def test_score_print(self):
        print(self.name, self.kor, self.math, self.eng)


s1 = student("홍길동", 100, 90, 80)
s2 = student("김길동", 90, 90, 30)

score = [
    s1,
    s2,
    student("최길동", 0, 0, 0),
    student("이길동", 70, 20, 100),
    student("박길동", 30, 60, 90),
]  # list에 객체를 넣어라... 변수없이 그냥 넣어드 댐

score[0].test_score_print() # 첫번째 학생의 모든 정보 출력 > 메소드 활용
print(score[2].kor) # 3번째 학생의 국어점수

print("---")

# 학생객체를 넣으면 학생 이름이 리턴되는 함수

# def name_return(s):
#     return s.name

# test = name_return(score[2])
# print(test)

# 람다대수 ㄱㄱ
test=(lambda s: s.name) (score[2])
print(test)

# 정렬(이름 ㄱㄴㄷ순)
score.sort(key=lambda s: s.name)
for s in score:
    s.test_score_print()

print("---")

# 3과목 평균값
score.sort(key=lambda s: (s.kor+s.math+s.eng)/3, reverse=True)
for s in score:
    s.test_score_print()