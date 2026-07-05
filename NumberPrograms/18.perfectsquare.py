n=int(input("enter a no :"))
d=n**0.5
if n==d**2:
    print("perfect square")
else:
    print("not a perfect square")
    start=1
    flag=False
    while start**2<=n:
        if start**2==n:
            flag=True
            break
        start+=1
        if flag:
            print("perfect square")
        else:
            print("not perfect square")