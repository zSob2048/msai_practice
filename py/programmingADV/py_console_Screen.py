
from py_object import product, seller


class console_screen:
    
    def page_main_print():
        print(" 1) 판매자 등록")
        print(" 2) 상품   등록")
        print(" 3) 판매자 일람")
        print(" 4) 상품   일람")
        print("...")
        print("10) 종료")
        return input("원하시는 업무 번호를 입력해주세요 : ")

    def page_1_print():
        print("-- 판매자 등록 --")
        name = input("이름          : ")
        addr = input("주소          : ")
        bday = input("생년월일(8자) : ")
        return seller(None, name, addr, bday)
    
    def page_2_print():
        print("-- 상품   등록 --")
        name = input("이름          : ")
        price = input("가격          : ")
        cate = input("품목          : ")
        s_no = input("판매자번호    :")
        return product(None, name, price, cate, s_no)
    
    def page_3_print(list):
        for sell in list:
            print(sell.no)
            print(sell.name)
            print(sell.addr)
            print(sell.bday)
        
    def page_4_print(list):
        for prod in list:
            print(prod.no)
            print(prod.name)
            print(prod.price)
            print(prod.cate)
            print(prod.s_no)
            print("---")
        
    def input_pagenum(page_all):
        return input("page (1 ~ %d) :" % page_all)
    
    def result_print(result):
        print(result)
    