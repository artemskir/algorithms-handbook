def greedy_algorithm():
    count = input()
    data_list = []
    for i in range(int(count)):
        data_local = tuple(map(int, input().split()))
        data_list.append(data_local)
    # choice by right line, example: [(1, 3), (6, 7)]
    data_list = buble_sort(data_list)
    data_list_new = data_list.copy()
    # delete all which intersect
    current = data_list[0]
    del_counter = 0
    for i in range(len(data_list) - 1):
        if current[1] >= data_list[i + 1][0]:
            del data_list_new[i + 1 - del_counter]
            del_counter += 1
        else:
            current = data_list[i + 1]
    return len(data_list_new)

def buble_sort(data_list):
    for i in range(len(data_list) - 1):
        for j in range(len(data_list) - 1 - i):
            if data_list[j][1] > data_list[j + 1][1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    return data_list

print(greedy_algorithm())