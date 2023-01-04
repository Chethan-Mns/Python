str1 = input()
index = int(input())
str2 = ""
for i in range(len(str1)):
    if i != index:
        str2 += str1[i]
print(str2)