# def b_sort(l):
#     for i in range(len(l)):
#         for j in range(i - 1):
#             if l[i] < l[j]:
#                 l[i], l[j] = l[j], l[i]


def b_sort_ex(l):
    for j in range(len(l) - 1):
        for i in range(len(l) - 1 - j):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]


def min_index(l):
    l_min = l[0]
    for i in range(1, len(l)):
        if l_min > l[i]:
            l_min = l[i]
    return l.index(l_min)


def s_sort(l):
    for i in range(len(l)):
        l[i + min_index(l[i:])], l[i] = l[i], l[i + min_index(l[i:])]


def s_sort_ex(l):
    for j in range(0,len(l)-1):
        min = l[j]
        min_inv = j
        for i in range(j+1, len(l)):
            if min > l[i]:
                min = l[i]
                min_inv = i
        l[j], l[min_inv] = l[min_inv], l[j]


l = [213, 765, 21, 1786, 2, 1, 6, 321, 32, 85, 899, 8963]
print(l)

# b_sort(l)
# b_sort_ex(l)
# s_sort(l)
s_sort_ex(l)


print(l)

l.sort() #그냥해줌
