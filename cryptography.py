'''
Cryptography
Requested files: crypto.py (Download)
Type of work: Individual work
Casper and John are US army soldiers. They are always sharing messages in Encrypted order of n messages. Ram an Indian soldier wants to find the message Casper and John share. Please help Ram to find out the secret message for n Encrypted messages using the list concept.

Input Format:
The first line of input consists of n messages
The next n lines of string input separated by space

Output Format:
The output consists of n lines of decoded messages with a new line. if n value is less than or equal to zero, print nothing.

Constraints:
1>=n>=50

Sample Input 1:
2
hsggthbuwvf
epdf

Sample Output 1:
codeshastra
code

Sample Input 2:
3
zov
brf
iaeflmgqx

Sample Output 2:
you
are
excellent

Sample Input 3:
-2

Sample Output 3:
'''

n = int(input())
lst, numbers, ord_val, asc, char = [], [], [], [], []
for i in range(n):
    m = input()
    lst.append(m)
if n in range(1, 51):
    for i in lst:
        for j in i:
            a = ord(j)
            asc.append(a)
        for j in reversed(range(len(i) // 2 + 1)):
            j = j - (2 * j)
            numbers.append(j)
        for j in range(1, (len(i) // 2) + 1):
            j = j - (2 * j)
            numbers.append(j)
        for j in range(len(i)):

            value = asc[j] + numbers[j]
            if value < 97:
                value = 123 + (numbers[j])
            ord_val.append(value)
        for j in ord_val:
            c = chr(j)
            char.append(c)
        char.append(" ")
        str1 = ''.join(map(str, char))
        numbers.clear()
        asc.clear()
        ord_val = []
    x = str1.split()
    for i in x:
        print(i)