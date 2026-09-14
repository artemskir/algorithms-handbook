# bubble sort
from typing import List


def sort(array: List[int]):
    for i in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                el = array[j]
                array[j] = array[j + 1]
                array[j + 1] = el
                swapped = True
        if not swapped:
            break
    return array

if __name__ == '__main__':
    print(sort([64, 34, 25, 12, 22, 11, 90]))