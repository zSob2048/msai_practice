
f = open ("C:/MS_AI_25/practice/py/kakaoTalkChats.txt","r",encoding="utf-8")
wordcount = {}
for line in f.readlines():
    # if line.startswith("2019"):
    #     break
    try:
        line = ''.join(line.replace("\n","").split(": ")[1:])
    except IndexError:
        if line.startswith("20"):
            continue
        line = line.replace("\n","").split(": ")[0]
        # continue
    # print(line)
    msg = line.strip().split()
    for word in msg:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
        # print(word)

print(wordcount)
f.close()

# 강사 필기랑 다름 