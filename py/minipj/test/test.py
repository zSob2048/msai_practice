class test_score:
    def __init__(self, t_c_no, q1, q2, q3, q4, q5, t_s_no):
        self.t_c_no = t_c_no
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5

        self.t_s_no = t_s_no
        self._score = 0


class test_correct:
    def __init__(self, c_no, q1, q2, q3, q4, q5):
        self.c_no = c_no
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
