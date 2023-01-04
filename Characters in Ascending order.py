str1 = input().lower()
lst = list(str1)
asc = []
final = []
str2 = ""
for i in lst:
    a = ord(i)
    asc.append(a)
asc.sort()
for i in asc:
    b = chr(i)
    final.append(b)
print(*final, sep= "")