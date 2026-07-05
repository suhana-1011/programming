#largest element in an list(max)
# l1=[10,5,3,8,4,80,7]
# if len(l1)>0:
#     m=l1[0]
#     for i in l1[1:]:
#         if i>m:
#             m=i
#     print(m)

#largest element in an list(min)
# l1=[10,5,3,8,4,80,7]
# if len(l1)>0:
#     m=l1[0]
#     for i in l1[1:]:
#         if i<m:
#             m=i
#     print(m)

# #sort the elements
# l1=[10,200,3,8,4,80,7]
# l1.sort()
# print(l1[-1],l1[0])

# #sorting the second largest
# l1=[10,5,3,4,8,80,7,80]
# l1=list(set(l1))
# l1.sort()
# print(l1[-2])

# #removing duplicates
# l1=[1,2,3,4,1,7,8,9,10,7,10]
# res=[] #keep this empty list since its fetching from l1
# for i in l1:
#     if i not in res:
#         res.append(i)
# print(res)

# #removing target from list
# l1=[1,2,3,1,1,1,1,4,5]
# target=int(input('target:'))
# for i in l1:
#     l1.remove(i)
# print(l1) ##this is the wrong method for removing target elements


#tracing
#'''1,2,3,1,1,1,1,4,5
#   i
# 2,3,1,1,1,1,4,5
#   i i
# 2,3,1,1,1,1,4,5
#       i
#2,3,1,1,1,1,4,5
#            i i'''


# #removing target elements from list using remove method correct logic
# l1=[1,2,3,1,1,1,1,4,5]
# target=int(input('target:'))
# res=[]
# for i in l1:
#     if i!=target:
#         res.append(i)
# print(res) 

###by using while loop
# l1=[1,2,3,1,1,1,1,4,5]
# target=int(input('target:'))
# while l1.count
# (target)>0:
#     l1.remove(target)
#     print(l1)

# l1=[1,2,3,1,1,1,1,4,5]
# target=int(input('target:'))
# i=0
# while i<len(l1):
#     if l1[i]==target:
#         l1.remove(target)
#     else:
#         i+=1
# print(l1)

# l1=[1,2,3,1,1,1,1,4,5]
# target=int(input('target:'))
# while i< l1:
#     if i in target:
#         for j in range(len(l1)):
#             l1[j]=l1[j+1] 
#     print(l1)

#using different approach
# l1=[1,4,7,4]
# for i in range(len(l1)-1):
#     l1[i]=l1[i+1]
# print(l1)

# another method
# l1=[1,2,3,1,1,1,1,4,5]
# target=int(input('target: '))
# while i>l1[ ]:
#     if i in target:
#         for j in range(len(l1)-1):
#             l1[j]=l1[j+1]
# print(l1)

#
l1=[1,2,3,1,1,1,1,4,5]
target=int(input('target: '))
i=0
while i<(len(l1)):
    if l1[i]==target:
        del l1[i]
    else:
        i+=1
print(l1)

#
# l1=[1,2,3,4,1,7,8,9,7,10]
# target=int(input('target: '))
# i=0
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[j]==l1[i]:
#             l1[j]=''
# while '' in l1:
#     l1.remove('')
# print(l1)

#
l1=[1,2,3,4,1,7,8,9,7,10]
for i in range(len(l1)):
    for j in range(i+1,len(l1)-1):
        if l1[j]==l1[i]:
            del l1[j]
print(l1)
