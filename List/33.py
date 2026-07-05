'''integer list'''
# l1=[2,1,3,4,5]
# count1=0
# count2=0
# for i in l1:
#     if i%2==0:
#          count1+=1
#     else:
#         count2+=0
# print(count1,count2)

'''integer list'''
# l1=[2,1,3,4,5,]
# ec,oc=0,0
# if i==0:
#     continue
# elif i%2==0:
#     ec+=i
# else:
    
#     oc+=i
# print(ec,oc)


# '''list intersection'''
# l1=[1,2,3,4,5,6,7,100,200]
# l2=[100,300,200,400,1,4,2000]
# print(list(set(l1).intersection(set(l2))))

'''list intersection'''
# l1=[1,2,3,4,5,6,7,100,200]
# l2=[100,300,200,400,1,4,2000]
# res=[]
# for i in l1:
#     if i in l2 and i not in res:
#         res.append(i)
# print(res)

# '''copy the list w/o using copy'''
# l1=[10,20,30,40]
# res=[]
# for i in l1:
#     res.append(i)
# print(res)

# '''no append no copy'''
# l1=[10,20,30,40]
# res=[]
# for i in l1:
#     res+=[i]
# print(res)


'''general copy/refrence copy'''
# l1=[10,20,30,40]
# res=l1
# for i in l1:
#     print(res)
# res[0]='don'
# print(res,l1)



# '''using list copy'''
# l1=[10,20,30,40]
# res=l1.copy()
# print(res)
# res[0]='don'
# print(res,l1)

# '''shallow copy using list:: '''
# l1=[10,20,30,40]
# res=l1[::]
# for i in l1:
#     print(res)
# res.append(2000)
# print(res,l1)

# '''deep copy we use it when dimensions are more '''
# import copy
# l1=[[10,20],[30,40]]
# l2=copy.deepcopy(l1)
# print(l1,l2)
# l1[0][0]=1000
# print(l1,l2)

'''move all zeros to end'''
# l1=[1,0,3,4,6,0,10,0]
# res=[]
# for i in l1:
#     if i!=0:
#         res.append(i)
# res=res+[0]*(len(l1)-len(res))
# print(res)

'''move all zeros to end using count of zero insted of len using list comprehension'''
l1=[1,0,3,4,6,0,10,0]
res=[i for i in l1 if i!=0]+[0]*l1.count(0)
print(res)

'''using append and pop'''
l1=[1,0,3,4,6,0,10,0,0,0,0]
for i in l1:
    if i==0:
        l1.remove(i)
        l1.append(i)
print(l1)



