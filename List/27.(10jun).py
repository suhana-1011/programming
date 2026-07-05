'''find 2nd largest without using sort()'''
l1=[1000,5,8,3,7,100,-300]
largest=min(l1)
sec_largest=min(l1)
for i in l1:
    if largest<i:
        sec_largest=largest
        largest=i
    elif i>sec_largest and i<largest:
        sec_largest=i
print(sec_largest)

'''find 2nd largest without using sort() using min max'''
l1=[1000,5,8,3,7,100,-300]
lar=max(l1)
sec=min(l1)
for i in l1:
    if i>sec and i<lar:
        sec=i
print(sec)   

'''find 2nd largest without using sort() without using min max'''
l1=[1000,5,8,215,3,100,7,100,-300,1000,200]
lar=0
sec=0
for i in range(len(l1)):
    if l1[i]>sec and l1[i]<lar:
        sec=l1[i]
    elif l1[i]>1:
        sec=1
        lar=l1[i]
print(sec)




