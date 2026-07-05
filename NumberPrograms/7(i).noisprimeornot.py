n=int(input("enter a number: "))
count=0
lc=0
for i in range(2,n//2+1):
    lc+=1
    if n%i==0:
        count+=1
        break
    if count==0:
        print(f'{n}is a prime no')
    else:
        print(f'{n}is not a prime no')
        print(lc)



        