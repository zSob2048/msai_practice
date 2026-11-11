from random import randint


# class User:
#     def input(self):
#         self.num = int(input("# :"))


# class CPU:
#     def start(self):
#         user = User()
#         self.cpu_num()
#         self.count = 0
#         while True:
#             self.user_num(user)
#             if not self.comparison(user):
#                 break

#     def cpu_num(self):
#         self.num = randint(1, 10000)

#     def user_num(self, user):
#         user.input()
#         if 0 < user.num < 10001:
#             return user.num
#         print(" 할생각있음? ")
#         return user.input()

#     def comparison(self, user):
#         self.count += 1
#         if user.num == self.num:
#             print("%d번만에 정답" % self.count)
#             return False
#         print("UP" if user.num < self.num else "DOWN")
#         return True


# g = CPU()
# g.start()


class Friend:
    def ask(self, user):
        user_ans_temp = user.tell()
        if 0 < user_ans_temp < 10001:
            return user_ans_temp
        return self.ask(user)

    def judge(self, game_ans, user_ans):
        if game_ans == user_ans:
            return False
        print("UP" if game_ans > user_ans else "DOWN")
        return True

    def think_ans(self):
        return randint(1, 10000)

    def tell_result(self, turn):
        print("%d번만에 정답" % turn)

    def start(self, user):
        turn = 0
        game_ans = self.think_ans()
        while True:
            turn += 1
            user_ans = self.ask(user)
            if not self.judge(game_ans, user_ans):
                break
        self.tell_result(turn)


class User:
    def tell(self):
        return int(input("#:"))


friend = Friend()
user = User()
friend.start(user)

# abc순 정렬+ 메인 역할 맨 아래

