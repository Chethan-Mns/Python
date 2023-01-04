import math
up,down,left,right = 0,0,0,0
while True:
    lst = input().split()
    direction = lst[0]
    if direction == "UP":
        value = int(lst[1])
        up += value
    elif direction == "DOWN":
        value = int(lst[1])
        down += value
    elif direction == "LEFT":
        value = int(lst[1])
        left += value
    elif direction == "RIGHT":
        value = int(lst[1])
        right += value
    elif direction == "STOP":
        break
    else:
        print("invalid Input")
x = up - down
y = right - left
output = math.sqrt((x ** 2) + (y ** 2))
print(round(output))