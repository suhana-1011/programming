n=int(input("enter a number:"))
while n>9:
    sum=0
    while n!=0:
        id=n%10
        sum+=id
        n=n//10
print(n)
