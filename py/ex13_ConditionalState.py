# 조건문 Conditional Statement
min = (float(input("중간고사:")) + float(input("기말고사:"))) / 2
print("---")
# print("평균점수: %.1f점" % ((float(input("중간고사:"))+float(input("기말고사:")))/2))
print("평균점수: %.1f점" % min)

# 프로그램 실행 순서를 바꿔야할때>> 제어문
# 제어문 ∋ 조건문 반복문 etc

# if, switch (python엔 X)
# if 조건식:        # 조건식에 괄호치면 가독?성?이? 좋아짐? ; 다른언어의 경우 문법상 써야됨
#   들여쓰기 내용
# else:             # : 포함 들여쓰기 없음
#   들여쓰기 내용

# # 평균점수가 90점 이상이면 잘했다!
# if min >= 90:
#     print("잘했다!")
#     a=10

# print(a) # >> 인터프리터방식이라 일단 가능, 조건에 맞지 않을 시... 실행시 err
# # Java(컴파일러방식)의 경우 정의 X(파일 자체 에러)

# 평균 점수가 80점 이상이면 잘했다
# 80점 안되면 나가
#   근데 70은 넘겼으면 열심히 해라
if min >= 80:
    print("잘했다")
else:
    print("나가")
    if min >= 70:
        print("열심히 해라")
# elif = else: if


# 점수가 90점 이상이면 수
if min >= 90:
    print("수")
elif min >= 80:
    print("우")
elif min >= 70:
    print("미")
elif min >= 60:
    print("양")
else:
    print("가")
