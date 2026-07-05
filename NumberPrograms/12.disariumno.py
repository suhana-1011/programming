n=int(input("enter a number:"))
dup1=n
dup2=n
count=0
sum=0
while n>0:
    count+=1
    n=n//10
    while dup1>0:
        ld=dup1%10
        sum+=ld**count
        count=count-1
        dup1=dup1//10
        if sum==dup2:
            print("disarium no")
        else:
            print("not disarium no")

# N diarium number

n = int(input("enter a number:"))
dup = n

s = str(n)
sum = 0

for i in range(len(s)):
    sum += int(s[i]) ** (i + 1)

if sum == dup:
    print("disarium no")
else:
    print("not disarium no")


#disarium no in range of 1 to n

n = int(input("enter n:"))

for num in range(1, n + 1):
    s = str(num)
    sum = 0

    for i in range(len(s)):
        sum += int(s[i]) ** (i + 1)

    if sum == num:
        print(num)


