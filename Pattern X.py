n = int(input())
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

for j in reversed(range(n -1)):
    print(" " * (n - j - 1) + "*" * (2 * j + 1))
