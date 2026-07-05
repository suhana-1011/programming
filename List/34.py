'''Find First and Last Occurrence of an Element in a List'''

def first_last_idx(l1,target):
    first_idx=-1
    last_idx=-1
    for i in range(len(l1)):
        if target==l1[i]:
            if first_idx==-1:
                first_idx=i
            last_idx=i
    return first_idx, last_idx
#l1=[1,2,3,7,11,3,5,6,3,12,14] #for 3=(2,8)
#l1=[11,7,8,6,2] #for 8=(2,2)
l1=[-1,8,9,10] 
#for 15=(-1,-1)
target=int(input('Target: '))
print(first_last_idx(l1,target))

'''WAP to find a product of elements in a list excluding the number in each iteration'''
l1=[2,4,6,8,10]
res=1
for i in l1:
    res=res*i
print([res//i for i in l1])

'''1. Count the total numbers of chars and numbers
2. Create a list which accepts the total values from count
3. Assign all the chars and numbers to new_list
4. Reverse the new_list
5. Assign the elements from new_list to old list only in place of chars and numbers'''

l1=['8','l','@','1','U','h','$','a','9','!','r','2','r']
print(l1)
cnt=0
for i in l1:
    if (ord(i)>=48 and ord(i)<=57) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90):
        cnt+=1
#print(cnt)
new_list=[None]*cnt
#print(new_list)

j=0
for i in range(len(l1)):
    if (ord(l1[i])>=48 and ord(l1[i])<=57) or (ord(l1[i])>=97 and ord(l1[i])<=122) or (ord(l1[i])>=65 and ord(l1[i])<=90):
        new_list[j]=l1[i]
        j+=1
#print(new_list)
new_list=new_list[::-1]
#print(new_list)

j=0
for i in range(len(l1)):
    if (ord(l1[i])>=48 and ord(l1[i])<=57) or (ord(l1[i])>=97 and ord(l1[i])<=122) or (ord(l1[i])>=65 and ord(l1[i])<=90):
        l1[i]=new_list[j]
        j+=1
print(l1)

'''ANOTHER WAY
1. Create a function which should return True if it is character or number, return False if it is special character
2. Call the function in each iteration by passing first element in list and last element in list
3. Swap the elements if it is True'''

def is_num_or_char(n):
