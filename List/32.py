'''linear search alg'''
# l1=[10,2,5,8,3,4]
# key=int(input('key:'))
# found=False
# for i in range(len(l1)):
#     if key==l1[i]:
#         print(f'{key}is found at index{i}')
#         found=True
#         break
# if not found:
#     print(f'{key} is not found')

# '''another method of linear serch python equi'''
# l1=[10,2,5,8,3,4]
# key=int(input('key:'))
# for i in range(len(l1)):
#     if key==l1[i]:
#         print(f'{key}is found at index{i}')
        
#         break
# else:
#     print(f'{key} is not found')


'''linear search alg using 2nd occerence'''
# l1=[10,2,5,8,3,4]
# key=int(input('key:'))
# count=0
# found=False
# for i in range(len(l1)):
#     if key==l1[i]:
#         count+=1
#         if count==2:
#             print(f'{key}is found at index{i}')
#             found=True
#             break
# if not found:
#     print(f'{key} is not found')

'''linear search alg using nth occerence'''
# l1=[10,2,5,8,3,4]
# n=int(input('n: '))
# key=int(input('key:'))
# count=0
# found=False
# for i in range(len(l1)):
#     if key==l1[i]:
#         count+=1
#         if count==n:
#             print(f'{key}is found at index{i}')
#             found=True
#             break
# if not found:
#     print(f'{key} is not found')

'''Binary search'''
#array must be sorted its divide and conquer method
l1=[10,20,30,40,50,60,70]
key=int (input('k:'))
first=0
last=len(l1)-1
found=False
while first<=last:
    mid=(first+last)//2
    if key<l1[mid]:
        last=mid-1
    elif key>l1[mid]:
        first=mid+1
    else:
        print(f'{key}is found at index{mid}')
        found=True
        break
if not found:
    print(f'{key} is not found')


