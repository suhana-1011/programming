'''String to Integer List Conversion'''
# s = '1 2 3 4 5'
# l1 = s.split()
# print(l1)
# res = []
# for i in l1:
#     res.append(int(i))
# print(res)


'''converts a list of string numbers into a list of integer numbers using map()'''
# l1=['1','2','3','4','5']
# res=map(int,l1)
# print(list(res))

'''cube of elements in a list using map() and a user-defined function.'''
# def cube(n):
#     return n**3
# l1=[1,2,3,4,5]
# res=map(cube,l1)
# print(list(res))

'''Input N elements into a list using map() *imp'''
# n=int(input('n: '))
# l1=list(map(int,input().split())) [:n] #n is used to remove unnecessary  for slicing
# print(l1)

'''Left Rotation of a List by One Position*imp'''
n=int(input('n: ')
l1=list(map(int,input( ).split())) [:n] 
temp=l1[0]
for i in range (len(l1)-1):
    l1[i]=l1[i+1]
l1[-1]=temp
print(l1)

'''Left Rotation of a List by K Positions'''
n=int(input('n: '))
l1=list(map(int,input().split()))[:n] 
k=int(input('k: '))%len(l1)
for val in range(k):
    temp=l1[0]
    for i in range(len(l1)-1):
        l1[i]=l1[i+1]
    l1[-1]=temp
print(l1)




'''Left Rotation of a List by K Positions Using Slicing'''
# n=int(input('n: '))
# l1=list(map(int,input().split()))[:n] 
# k=int(input('k: '))%len(l1)
# for val in range(k):
#  l1=l1[1:]+l1[:1]
# print(l1)

'''Right Rotation of a List by One Position'''
# n=int(input('n: '))
# l1=list(map(int,input( ).split())) [:n] 
# temp=l1[-1]
# for i in range (len(l1)-1,0,-1):
#     l1[i]=l1[i-1]
# l1[0]=temp
# print(l1)

'''Right Rotation of a List by K Positions'''
# n=int(input('n: '))
# l1=list(map(int,input().split()))[:n] 
# k=int(input('k: '))%len(l1)
# for val in range(k):
#     temp=l1[-1]
#     for i in range (len(l1)-1,0,-1):
#         l1[i]=l1[i-1]
#     l1[0]=temp
# print(l1)


'''Accept N elements and K value from the user using slicing'''
# n=int(input('n: '))
# l1=list(map(int,input().split()))[:n] 
# k=int(input('k: '))%len(l1)
# l1=l1[-k:]+l1[:-k]
# print(l1)

#codingbat list1 and 2




