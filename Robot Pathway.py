import math
x, y = 0, 0
while True:
    try:direction, n = input().upper().split()
    except:break
    units = int(n)
    if direction == "UP":y += units
    elif direction == "DOWN":y -= units
    elif direction == "LEFT":x -= units
    elif direction == "RIGHT":x += units
print(round(math.sqrt((x ** 2) + (y ** 2))))
