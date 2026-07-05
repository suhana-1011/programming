'''2sumproblem'''
l1=[2,1,3,6,5,1,4]
target=int(input('Target: '))
def twosum(l1,target):
    for i in l1:
        for j in range(i+1,len(l1)):
            if l1[i]+l1[j]==target:
                print (i,j)
            break
twosum(l1,target)

'''divide list2halves'''
l1=[2,1,3,6,5,1,4]
target=int(input('Target: '))
def twosum(l1,target):
    for i in l1:
        for j in range(i+1,len(l1)):
            if l1[i]+l1[j]==target:
                print (i,j)
            break
twosum(l1,target)
 
#Sum of Prime numbers in a given list
def is_prime(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
cnt=0
l1=[2,1,3,6,5,1,4,7]
for i in range(len(l1)):
    if is_prime(l1[i]):
        cnt+=l1[i]
print("Sum of Prime Numebrs: ",cnt)

'''move zeros'''
l1=[1,0,3,4,6,0,10,0]
res=[]
for i in l1:
    if i!=0:
        res.append(i)
res=res+[0]*(len(l1)-len(res))
print(res)

l1=[1,0,3,4,6,0,10,0]
res=[i for i in l1 if i!=0]+[0]*l1.count(0)
print(res)

l1=[1,0,0,0,0,0,0,0,3,4,6,0,10,0]
for i in l1:
    if i==0:
        l1.remove(i)
        l1.append(i)
print(l1)

l1=[1,1,0,0,0,1,1,0,1,0,1]
for i in l1:
    if i==0:
        l1.remove(i)
        l1.append(i)
print(l1)


 
#wap to check second list is a child of first list or not
#o/p: l2=[3,4,5] in proper sequence
def function(l1,l2):
    for i in range(len(l1)):
        if l1[i:i+len(l2)]==l2:
            return True
    return False
l1=[1,2,3,4,5,6,7,8]
l2=[3,4,5]
if function(l1,l2):
    print("L2 is a child of L1")
else:
    print("L2 is not a child of L1")


'''self'''
#if (list(set(l1).intersection(l2))):
    #print("L2 is a child of L1")
#print("L2 is not a child of L1")

#WAP to display the union of 2 list
l1=[1,2,3,4,5,6]
l2=[5,6,7,8,1]