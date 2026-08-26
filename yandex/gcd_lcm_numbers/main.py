number_a, number_b = map(int, input().split())

def gcd_compute(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)

print(gcd_compute(number_a, number_b))