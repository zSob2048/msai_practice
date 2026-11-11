


q_ans = []
q_pt = []
for i in range(5):
    print(" %d번 문항 " % (i+1))
    q_ans += input("답   :")
    q_pt += input("배점 :")

print(q_ans,q_pt)