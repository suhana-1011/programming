#sum_of_given_no
n=int(input("enter a number:"))
sum=0
while n>0:
    lastdigit=n%10
    sum+=lastdigit
    n=n//10
    print(sum)