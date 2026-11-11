# 2 class

# from ex33_oop_1 import mouse
# # (위에두면 무한루프라고 에러뜸)

class book :
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info_print(self):
        print(self.name, self.price)


# from ex33_oop_1 import mouse
# # 이 자리에 ex33_1을 들어오는 상태

# m = mouse("로지텍123", 10000)
# m.info_print()

if __name__ == "__main__":
    from ex33_oop_1 import mouse

    m = mouse("로지텍123", 10000)
    m.info_print()
# >> import시 이 실행영역까지 뜨는걸 방지하기 위해...
# >> main 영역을 만들어버리는 느낌

