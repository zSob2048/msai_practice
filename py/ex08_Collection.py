# collection
# 변수: int float str bool 어쩌고... >> 변수 1: 데이터 1
# 변수 1: 데이터 n >> 컬렉션... matrix..?
# List계열 ; list
# Set계열  ; set
# Map계열  ; dict
# 이외에 다양하게 있음 python에
# 학생 1명의 국어 점수 80
kor = 80
print(kor, type(kor), id(kor))

# list : []
kor_list = [90, 50, 30, 11, 60, 50, 35, 0, 100, 98]
print(kor_list, type(kor_list), id(kor_list))
print(len(kor_list))  # 갯수세기; 10
print(kor_list[1])  # n번항(0번부터) ; 50
print(kor_list.index(50))  # ↑ 의 역함수 ; 1... 만나오는데
print(kor_list[2:5])  # n:k> n번부터 (k-n)회 (기본 +1) ; [30, 11, 60]
print(kor_list[3:8:2])  # n:k:r n번부터 (K-n)/r회 r칸씩 ; [11, 50, 0]
print(kor_list[:8:2])  # 생략가능(0번부터)
print(kor_list[3::2])  # 생략가능(끝까지)
print(kor_list[3:8:])  # 생략가능(1칸씩)
print(kor_list[::2])  # 가능
print(kor_list[::-1])  # 역순
# str에서 특정 글자에 접근할 때 list와 비슷하게 작동...
kor_list.append(50)  # .append(n) ; 뒤에 n 추가
kor_list.insert(2, 40)  # .insert(n, NN) ; n번자리에 NN추가(이후 1칸씩 밀림): 특정위치에 추가
kor_list[0] = 100  # 수정
del kor_list[1]  # 삭제

print("---")
# set : {} ; 집합
eng_set = {90, 50, 30, 11, 60, 50, 35, 0, 100, 98}
print(eng_set, type(eng_set), id(eng_set))
print(len(eng_set))
# 순서가 랜덤이라 잘 사용하지 않음 oO뭐그렇겠지...

print("---")
# dictionary : {:} ; 순서x, 키 - 값 형태
mat_dict = {"홍길동": 100, "김길동": 50, "최길동": 30}
print(mat_dict, type(mat_dict), id(mat_dict))
print(mat_dict["김길동"])

# collection 이어서
# list가 주력, python은 형변환이 쉽다> set으로 변환시켜 중복을 없에는데 사용 可 > 다시 list로 변환해 사용

# dict : 키-값
score = [[[[70, 30], 100], [50, 50], [80, 30]], [100, 20, 30], [90, 30, 5]]
print(score[0][0][0])  # 다차원list > 알아보기 힘듬

student = {"홍길동": {"국어": 50, "영어": 30}, "김길동": 80}
print(student["김길동"])
print(student["홍길동"]["국어"])
# >> dict+list 조합을 사용
print(student.keys())  # 키값 추출 = 역함수 # dict_keys(['홍길동', '김길동'])
# >> list로 바꿔서 사용 print(list(student.keys()))

print("최길동" in student)  # 유무 T/F # 키값에만 작용

# ---
# python에만 있는 collection ;
# range : 범위
a = range(10)  # 0 ~ n회 ; n-1까지)
a = range(2, 10)  # (n,k)> n ~ (k-n)회 
a = range(2, 10, 3)  # (n,k,r)> n ~ (k-n)/r회 r단위로
print(a, type(a))
# list 1 ~ 20 > 규칙적인 list가 필요시...
b = list(range(1, 21))
print(b)

# tuple
c = (10, 10, 30, 2, 50)
print(c, type(c))
print(c[2])
# python의 특수한 문법의 기반이 된다...

x = 10
y = 20
# y=x 대칭시키려면... > 타 언어의 경우 변수 추가할당..
(x, y) = (y, x)  # 열벡터같은느낌인가
q, w, e = 1, 3, 5  # 변수 할당 한번에... 괄호 생략도 가능
