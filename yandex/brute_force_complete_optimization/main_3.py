n_value, k_value = map(int, input().split())


def combination(n, k):
    # (k + n - 1)!
    nomirator = 1
    for number in range(1, k_value + n_value):
        nomirator *= number
    # (n - 1)! * k!
    denominator_1 = 1
    for number in range(1, n_value):
        denominator_1 *= number
    denominator_2 = 1
    for number in range(1, k_value +1):
        denominator_2 *= number

    return nomirator // (denominator_1 * denominator_2)


print(combination(n_value, k_value))
