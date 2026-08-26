count = int(input())
data = list(map(int, input().split()))

def split_sort(data):
    if len(data) <= 1:
        return data

    mid_point = len(data) // 2
    left, right = data[:mid_point], data[mid_point:]
    sorted_left = split_sort(left)
    sorted_right = split_sort(right)

    return merge(sorted_left, sorted_right)

def merge(arr1, arr2):
    i, j = 0, 0
    output_array = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            output_array.append(arr1[i])
            i += 1
        else:
            output_array.append(arr2[j])
            j += 1
    output_array.extend(arr1[i:])
    output_array.extend(arr2[j:])
    return output_array

print(' '.join(str(number) for number in split_sort(data)))