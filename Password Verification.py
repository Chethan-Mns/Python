lst = input().split(",")
small, capital, num, special = 0, 0, 0, 0
lst2, result = [], []
for str1 in lst:
    str1 = str1.lstrip()
    if len(str1) in range(6, 13):
        lst2.append(str1)
for str1 in lst2:
    for j in str1:
        if j.islower():
            small += 1
        elif j.isupper():
            capital += 1
        elif j.isdigit():
            num += 1
        else:
            special += 1
    if num >= 1 and small >= 1 and capital >= 1 and special >= 1:
            result.append(str1)
    small, capital, num, special = 0, 0, 0, 0
    
if len(result) == 0:
    print("No password matches the condition")
elif len(result) != 0:    
    print(" ", end="")
    print(*result,sep=",")