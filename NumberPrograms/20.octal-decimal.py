#decimal-octal
n = int(input("enter a decimal number:"))
octal = ""

while n > 0:
    rem = n % 8
    octal = str(rem) + octal
    n = n // 8

print(octal)

#octal to decimal

n = int(input("enter an octal number:"))
sum = 0
p = 0

while n > 0:
    lastdigit = n % 10
    sum += lastdigit * (8 ** p)
    p += 1
    n = n // 10

print(sum)