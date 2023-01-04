str1 = input()
numbers = 0
for i in range(len(str1)):
    if str1[i].isdigit():
        numbers += 1
print("Characters = ",len(str1) - numbers)
print("Digits = ",numbers)