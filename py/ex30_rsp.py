from random import randint


# class User:
#     def rsp_out(self):
#         return input("YOU\t: ")


# class CPU:
#     def rsp_in(self, user, rsp):
#         user_ans_temp = user.rsp_out()
#         if user_ans_temp in rsp:
#             return rsp.index(user_ans_temp)
#         print("입력한 값을 확인하세요.\n---")
#         return self.rsp_in(user, rsp)

#     def rsp_judge(self, cpu_out, user_out):
#         judge = (user_out - cpu_out) % 3
#         wdl = ["draw", "win", "lose"]
#         print(wdl[judge])
#         return judge

#     def rsp_out(self, rsp):
#         cpu_out = randint(0, 2)
#         print("CPU\t: %s" % rsp[cpu_out])
#         return cpu_out

#     def rsp_start(self, user):
#         rsp = ["가위", "바위", "보"]
#         win = 0
#         while True:
#             user_out = self.rsp_in(user, rsp)
#             cpu_out = self.rsp_out(rsp)
#             judge = self.rsp_judge(cpu_out, user_out)
#             if judge == 2:
#                 print("%d연승" % win)
#                 break
#             win += judge
#             print("---")


# user = User()
# cpu = CPU()
# cpu.rsp_start(user)


class Refree:

    def __init__(self):
        self.rule = [None, "가위", "바위", "보"]

    def p1_call(self):
        return Player_random()

    def p2_call(self):
        return Player_input()

    def p1_submit(self, p1):
        return p1.submit()

    def p2_submit(self, p2):
        p2_temp = p2.submit()
        if 0 < p2_temp < 4:
            return p2_temp
        return self.p2_submit(p2)

    def rule_print(self):
        for i, v in enumerate(self.rule):
            if i != 0:
                print("%d) %s" % (i, v))
        print("---")

    def submit_print(self, p1_sub, p2_sub):
        print("P1: %s" % self.rule[p1_sub])
        print("P2: %s" % self.rule[p2_sub])

    def judge(self, p1_sub, p2_sub):
        t = p1_sub - p2_sub
        if t == 0:
            print("무")
            return 0
        elif t == -1 or t == 2:
            print("패")
            return 2
        else:
            print("승")
            return 1

    def result_print(self, win):
        print("%d연승" % win)

    def start(self):
        p1 = self.p1_call()
        p2 = self.p2_call()
        self.rule_print()
        win = 0
        while True:
            p1_sub = self.p1_submit(p1)
            p2_sub = self.p2_submit(p2)
            self.submit_print(p1_sub, p2_sub)
            t = self.judge(p1_sub, p2_sub)
            if t == 2:
                break
            win += t
            print("---")
        self.result_print(win)


class Player_random:
    def submit(self):
        return randint(1, 3)


class Player_input:
    def submit(self):
        return int(input("뭐: "))


r = Refree()
r.start()
