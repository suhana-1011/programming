n=int(input("enter a number :"))
num=n+1
start=1
flag=False
while start**2<=num:
    if start**2==num:
        
            flag=True
            break
        start+=1
    if flag:
          print("perfect square")
else:
    print("not a perfect square")