for _ in range(int(input())):
    string, result = input().lower(), ""
    alp = list("abcdefghijklmnopqrstuvwxyz")
    mid = len(string) // 2
    temp = mid
    for i in range(len(string)):
        if i < mid:
            result += alp[alp.index(string[i]) - temp]
            temp -= 1
        elif i == mid:
            result += string[i]
            temp += 1
        else:
            result += alp[alp.index(string[i]) - temp]
            temp += 1
    print(result)
