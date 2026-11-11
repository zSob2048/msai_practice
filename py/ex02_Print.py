# 출력 ; 중간 테스트용

# 콘솔창(*아래 출력창) 에 ㅋ ㅎ 출력

print("ㅋ")
print('ㅎ')

# python의 경우 " " 와 ' ' 구분 X... 주로 " " 사용 ; art shift F< 쓰면 다 ""로바꿔줌

print("ㅋ", end=" ") # 줄변경 제외 , end="" : 기본값이 end = "\n" 
print('ㅎ')

# 콘솔창에 / 출력
# 콘솔창에 - 출력
print("/")
print("-")

# 콘솔창에 \ 출력
# 콘솔창에 " 출력
print("\\") # \\ = \ > 경로 작성 등...
print("\"") # \" = "
print('"') # python은 가능

# > 문법적으로 용도가 할당되어 있는 문자의 경우 단일 문자로 출력 불가능 > 작성 시 확인

# 이 외 \ back-slash(역슬래쉬) 문법
print("aaa\nb") # \n = new line, 줄바꿈
print("aaa\rb") # \r = carrage return, 커서를 맨 앞으로 ; insert
print("aaa\r\nb") # >enter와 동일해짐 ( \n의 경우 띄어쓰기 line 포함 줄 만 바꿔짐 *언어에 따라 자동으로 땡겨줌 )
print("aaa\tb") # \t = tab, 줄 정렬에 용이
print("aaa\bb") # \b = backspace( 1byte )
print("aaa\b") # * C 기준 영어 1글자 = 1byte / Python 기준 영어 1글자 = 2bytes > 정상작동안함...

