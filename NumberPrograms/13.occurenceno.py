n=int(input("enter a number:"))
d1={}
while n!=0:
    id=n%10
    if id not in d1:
        d1[id]=1
    else:
        d1[id]+=1
        n=n//10
        for k,v in d1. items():
            print(k,"->",v)