def is_prime(n):
    if n < 2:
        return False

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            break
    else:
        return True

    return False


N = int(input())

for number in range(2, N + 1):
    if is_prime(number):
        print(number, end=" ")

print()