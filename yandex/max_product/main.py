count = int(input())
data = list(map(int, input().split()))

data_output = 0

def gen_numbers(from_number, to_number):
    global count, data
    count = to_number
    for i in range(from_number, to_number):
        data.append(i ** 2)

# gen_numbers(int(input()), int(input()))

index_1 = 0
for i in range(1, len(data)):
    if data[i] > data[index_1]:
        index_1 = i
index_2 = 0

if index_1 == 0:
    index_2 = index_1 + 1

for i in range(1, len(data)):
    if index_1 != i and data[i] > data[index_2]:
        index_2 = i

data_output = data[index_1] * data[index_2]
print(data_output)