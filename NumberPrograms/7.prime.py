#factors_of_no
n=int(input("enter a number:"))
count=0
for i in range (1,n+1):
    if n%i==0:
        count+=1
        print(count)
        if count==2:
            print("prime number")
        else:
            print("not a prime number")

# if n>1:
#     for i in range (2,n):
#         if n%i==0:
#             print("not a prime number")
#             break
#         else:
#             print("prime")
#     else:
#         print("not a prime")

            