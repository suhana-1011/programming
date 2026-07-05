n=int(input("enter a no:"))
decimal=0
p=1
while n>0:
    rem=n%10
    decimal=decimal+p
    
    n=n//2
    p*=2
    print(decimal)

#decimal-to binary

n=int(input("enter a no:"))
bin=0
temp=1
while n!=0:
    id=n%2
    bin=bin+temp*id
    temp=temp*10
    n=n//2
    print(bin)

