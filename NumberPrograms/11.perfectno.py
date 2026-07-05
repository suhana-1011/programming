#it is aperfect number or not
n=int(input("enter a number:"))
dup=n
sum=0
for i in range (1,n):
    if n%i==0:
        sum+=i
        if sum==dup:
            print("perfect no")
        else:
            print("not perfect no")

#perfect no in range of 1 to n

n = int(input("enter n:"))

for num in range(1, n + 1):
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        print(num)

#N perfect number

n = int(input("enter a number:"))
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("perfect no")
else:
    print("not perfect no")



