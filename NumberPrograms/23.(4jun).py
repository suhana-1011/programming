# count_of_digit(n)
n=int(input("n:"))
c=0
while n>0:
    c+=1
    n//=10
    print(c)
#or using typecasting
n=int(input("n:"))
print(len(str(n)))


n=int(input("enter n: "))
if str(n)==str(n)[::-1]:
    print('palindrome')
else:
    print("not a palindrome")

#gcd/hcf
n1=int(input("enter n1: "))
n2=int(input("enter n2: "))
hcf=1
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        hcf=i
        print(hcf)

#using built in method in gcd
import math
n1=int(input("enter n1: "))
n2=int(input("enter n2: "))
print(math.gcd(n1,n2))

#lcm
n1=int(input("enter n1: "))
n2=int(input("enter n2: "))
lcm=None
lc=0
i=max(n1,n2)
while True:
    if i%n1==0 and i%n2==0:
         lcm=i
         break
    i+=1
print(lcm)
print(lc)

#using built in method in gcd
import math
n1=int(input("enter n1: "))
n2=int(input("enter n2: "))
print(math.lcm(n1,n2))


   




