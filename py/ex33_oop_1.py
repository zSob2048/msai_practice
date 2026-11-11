# 1 objectt
# 제목이 뭐시기인 

class mouse:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info_print(self):
        print(self.name, self.price)    
        

if __name__ == "__main__":
    from ex33_oop_2 import book
    # from py.ex33_oop_2 import book # vscode에서 자동으로 py(파일명).이런거 붙여주는데 떼고 쓰면 됨


    b = book("점프 투 파이썬", 30000)
    b.info_print()

