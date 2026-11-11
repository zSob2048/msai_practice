# # f = open("C:\\MS_AI_25\\practice\\py") # 경로 \\ 2개써야댐
# msg = input(":")
# f = open("C:/MS_AI_25/practice/py/ex40.txt", "a", encoding="utf-8") # 이래도 됨

# # open(경로, mod, 인코딩=)
# # r: read / w: write(매번 새로작성) / a: append(뒤에 추가식 작성)

# # 인코딩 : 데이터를 전기신호로
# # 디코딩 : 전기신호를 데이터로
# # 인코딩 - 디코딩 방식이 맞아야댐
# # utf-8 : 세계적으로 만이씀! + 리눅스가 utf-8
# # euc-kr : utf-8 다음으로 만이씀( 국내기준, windows가 7~8즘에 이게 주력이다가 요즘엔 utf-8써서)

# f.write(msg+"\n") # 그냥은 바로뒤에붙으

# # 확장자 : 으디에서열면 제일 ㄱㅊ게 열리는 파일!!
# # 윈도우에만 이씀!!

# # WORA (Write Once, Run Anywhere)
# # >> 원래는 시스템별로 프로그램을 다 다르게 만들어야... >WORA를 지원하면 다른부분은 안만들어도 ㄱㅊ,>>하나로 아무데서나 ㄱㄴ
# # 근데어차피경로가다른데

####################################################

# f = open("C:/MS_AI_25/practice/py/ex40.txt", "r", encoding="utf-8")

# data = f.read()
# print(data, type(data)) # 전체 다 읽어서 str로

# data = f.readline()
# print(data, type(data))  # 한줄씩 할때마다 다음줄 읽어줌 str
# data = f.readline()
# print(data, type(data))  # 다음 줄 읽어주는거고 한줄읽어주는거아님 전부읽고 다음줄읽으면 안나옴

# data = f.readlines()
# print(data, type(data)) # 전체 다 읽어서 \n 기준으로 나눠서 list로 ; \n이 남아있어서 치우고 써야댐

# f.close()

# # with open("") ; 알아서 닫아주는~

####################################################
import re


f = open("C:/MS_AI_25/practice/py/ex40_c.csv", "a", encoding="utf-8")

while True:
    c_name = input("이름 : ")
    if c_name == "그만":
        break
    c_price = input("가격 : ")
    c_mass = input("중량 : ")
    print("---")
    f.write("%s,%s,%s\n" % (c_name, c_price, c_mass))

###################################################
f = open("C:/MS_AI_25/practice/py/ex40_c.csv", "r", encoding="utf-8")
# for line in r