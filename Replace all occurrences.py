str1 = input()
char = input()
index = str1.index(char)
special = input()
str2 = ""
for i in range(len(str1)):
    if i == index:
        str2 += special
    else:
        str2 += str1[i]
print("Modified string:")
print(str2)