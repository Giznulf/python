def rec(list):
    if len(list) == 0:
        return
    i = list.pop(-1)
    rec(list)
    print(i)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

rec(my_list)