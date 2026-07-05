n=int(input("enter a number:"))
dup=n
sum=0

while n>0:
    lastdigit=n%10
    prod=1
    for i in range(1,lastdigit+1):
        prod*=i
    sum+=prod
    n=n//10
    if dup==sum:
        print("strong no")
    else:
        print("not strong no")


#strong in range of 1 to n

n = int(input("enter n:"))

for num in range(1, n + 1):
    dup = num
    sum = 0

    while num > 0:
        lastdigit = num % 10

        prod = 1
        for i in range(1, lastdigit + 1):
            prod *= i

        sum += prod
        num = num // 10

    if dup == sum:
        print(dup)

# n strong no
n = int(input("enter a number:"))
dup = n
sum = 0

while n > 0:
    lastdigit = n % 10

    fact = 1
    for i in range(1, lastdigit + 1):
        fact *= i

    sum += fact
    n = n // 10

if dup == sum:
    print("strong no")
else:
    print("not strong no")
