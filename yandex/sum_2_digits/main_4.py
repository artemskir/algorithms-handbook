count_n, count_m = map(int, input().split())

data_a = []
data_b = []
data_output = [[] for _ in range(count_n)]
control = False

for i in range(count_n * 2):
    if not control:
        data_a.append(list(map(int, input().split())))
    else:
        data_b.append(list(map(int, input().split())))
    if i == count_n - 1:
        control = not control

for i in range(count_n):
    for j in range(count_m):
        data_output[i].append(data_a[i][j] + data_b[i][j])

for data in data_output:
    print(' '.join(str(i) for i in data))