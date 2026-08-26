count_groups = int(input())

data_group = []

for _ in range(count_groups):
    count = input()
    data_group.append(list(map(int, input().split())))

def processing_parts(arr1, arr2):
    i = 0
    j = 0
    arr_merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr_merged.append(arr1[i])
            i += 1
        else:
            arr_merged.append(arr2[j])
            j += 1
    arr_merged.extend(arr1[i:])
    arr_merged.extend(arr2[j:])
    return arr_merged

init_arr = data_group[0]
for i in range(1, len(data_group)):
    init_arr = processing_parts(init_arr, data_group[i])

print(' '.join(str(number) for number in init_arr))