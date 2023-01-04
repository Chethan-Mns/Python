n = int(input())
for i in reversed(range(n)):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))