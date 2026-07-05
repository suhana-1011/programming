#factors_of_no
n=int(input("enter a number:"))
for i in range (1,n+1):
    if n%i==0:
        print(i)
sum=0
for i in range (1,n+1):
    if n%i==0:
        sum+=i
        print(sum)
        # print(sum([x for x in range (1,n+1)if n%x==0]))