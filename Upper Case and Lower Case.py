str1 = input()
upper = 0

for i in range(len(str1)):
    if str1[i].isupper():
        upper += 1
lower = len(str1) - upper
print(upper)
print(lower)