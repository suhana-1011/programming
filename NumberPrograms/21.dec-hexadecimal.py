#decimal to hexadecimal 

n = int(input("enter a decimal number:"))
hexa = ""

digits = "0123456789ABCDEF"

while n > 0:
    rem = n % 16
    hexa = digits[rem] + hexa
    n = n // 16

print(hexa)

#hexadecimal to decimal

n = input("enter a hexadecimal number:").upper()

digits = "0123456789ABCDEF"
sum = 0
p = 0

for i in range(len(n)-1, -1, -1):
    sum += digits.index(n[i]) * (16 ** p)
    p += 1

print(sum)



