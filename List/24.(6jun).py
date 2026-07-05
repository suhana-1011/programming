#basic list programs
#creating homogeneous list
n=int(input("enter n: "))
l1=[int(input("val: ")) for i in range(n)]
print(l1)

#creating heterogeneous list
n=int(input("enter n: "))
l1=eval(input( ))
print(l1,type(l1))

#by using map
l1=list(map(complex,input().split()))
print(l1)