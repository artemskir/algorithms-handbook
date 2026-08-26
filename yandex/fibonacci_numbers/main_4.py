n_number = int(input())

def fibonacci_mod(n):
    period = 60
    n = n % period

    if n == 0:
        return 0

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current

number = fibonacci_mod(n_number + 2)
last_digit = (number - 1) % 10
print(last_digit)