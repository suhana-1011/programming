n=int(input("enter a number:"))
dup=n
sum=0

while n>0:
    lastdigit=n%10
    sum=(sum+lastdigit**3)
    n=n//10
    if sum==dup:
        print("armstrong no")
    else:
        print("not armstrong no")

#armstrong in range of 1 to n

n = int(input("Enter n: "))

for num in range(1, n + 1):
    dup = num
    temp = num
    sum = 0

    while temp > 0:
        lastdigit = temp % 10
        sum = sum + lastdigit ** 3
        temp = temp // 10

    if sum == dup:
        print

#N armstrong no

n = int(input("Enter n: "))

for num in range(1, n + 1):
    dup = num
    digits = len(str(num))
    sum = 0

    while dup > 0:
        lastdigit = dup % 10
        sum = sum + lastdigit ** digits
        dup = dup // 10

    if sum == num:
        print(num)


