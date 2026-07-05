'''bubble sort for ascending'''
# l1=[5,4,300,2,1,-100,-5]
# print(l1)
# for i in range(len(l1)-1):
#     for j in range(len(l1)-1-i):
#         if l1[j]>l1[j+1]:  #for ascending 
#             l1[j],l1[j+1]=l1[j+1],l1[j]


# '''bubble sort for descending'''
# l1=[5,4,300,2,1,-100,-5]
# print(l1)
# for i in range(len(l1)-1):
#     for j in range(len(l1)-1-i):
#         if l1[j]<l1[j+1]:  #for descending 
#             l1[j],l1[j+1]=l1[j+1],l1[j]


'''Insertion Sort for ascending'''
l1=[23,1,10,5,2]
for i in range(1,len(l1)):
    key=l1[i]=l1[i]
    j=i-1
    while j>=0 and key<l1[j]:   #i++ and j--
        l1[j+1]=l1[j]
        j-=1
        l1[j+1]=key
    print(l1)

'''Insertion Sort for descending'''
l1=[23,1,10,5,2]
for i in range(1,len(l1)):
    key=l1[i]=l1[i]
    j=i-1
    while j<0 and key>l1[j]:
        l1[j+1]=l1[j]
        j-=1
        l1[j+1]=key
    print(l1)




