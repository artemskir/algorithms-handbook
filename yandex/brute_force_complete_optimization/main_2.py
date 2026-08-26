n_value, k_value = map(int, input().split())


def combination(n, k):
    # n!
    numerator = 1
    for number in range(1, n_value + 1):
        numerator *= number
    # (n - k)! * k!
    denominator_1 = 1
    for number in range(1, n_value - k_value + 1):
        denominator_1 *= number
    denominator_2 = 1
    for number in range(1, k_value + 1):
        denominator_2 *= number
    denominator = denominator_1 * denominator_2
    return numerator // denominator


print(combination(n_value, k_value))
