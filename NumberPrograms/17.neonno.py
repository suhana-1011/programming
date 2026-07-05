n=int(input("enter a number:"))
num=n**2
sum=0
while num!=0:
    id=num%10
    sum+=id
    num=num//10
    if sum==n:
        print("neon no")
    else:
         print("not neon no")