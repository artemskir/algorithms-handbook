degree_1 = int(input())
data_1 = list(map(int, input().split()))

degree_2 = int(input())
data_2 = list(map(int, input().split()))

def sum_polynomials(A, B):
    output_array = []
    output_degree = max(degree_1, degree_2)
    biggest, smallest = [], []
    if len(A) > len(B):
        biggest = A
        smallest = B
    else:
        biggest = B
        smallest = A
    if biggest != smallest:
        for i in range(len(biggest) - len(smallest)):
            smallest.insert(0, 0)
    stop_flag = False
    for i in range(len(biggest)):
        if biggest[i] == 0:
            if not stop_flag:
                output_degree -= 1
        else:
            stop_flag = True
        output_array.append(biggest[i] + smallest[i])


    return output_degree, output_array

degree, array = sum_polynomials(data_1, data_2)
print(degree)
print(' '.join(str(number) for number in array))