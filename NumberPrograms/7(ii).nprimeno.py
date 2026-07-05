n= int(input("enter a number: "))
prime_no_count=0
val=2
while True:
    count=0
    for i in range(2,val//2+1):
        if val%i==0:
            count+=1
            break
        if count==0:
            print(val,end='')
            prime_no_count+=1
            if prime_no_count==n:
                break
            val+=1
    