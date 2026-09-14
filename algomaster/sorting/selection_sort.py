# selection sort
from typing import List
import math

def sort(arr: List[int]):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == '__main__':
    print(sort([29, 10, 14, 37, 13, 8]))