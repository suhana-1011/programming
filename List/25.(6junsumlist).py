# l1=[1,2,3,8,7]
# res=0
# for i in l1:
#     res+=i
#     print(res)

# l1=[1,2,3,8,7,'don']
# res=0
# for i in l1:          #type error 
#     res+=i
#     print(res)

# l1=[1,2,3,8,7,'don',1+2j,1.7,True]
# res=0
# for i in l1:
#     if type(i)==int or type(i)==float: 
#          res+=i
# print(res)

#by using isinstance
# l1=[1,2,3,8,7,'don',1+2j,1.7,True]
# res=0
# for i in l1:
#     if isinstance(i,(int,float)):
#          res+=i
# print(res)


#2.product of list using homogeneous
# l1=[1,2,3]
# res=1
# for i in l1:
#     if isinstance(i,(int,float)):
#          res*=i
# print(res)

# diff logic
# l1=[10,5,8,3]
# res=l1[0]
# for i in range (1,len(l1)):
#       res-=l1[i]
# print(res)

l1=[]
if len(l1)>0:
   res=l1[0]
   for i in range (1,len(l1)):
      res-=l1[i]
   print(res)


#product of list using heterogeneous
# l1=[1,2,3,8,7,'don',1+2j,1.7,True]
# res=1
# for i in l1:
#     if isinstance(i,(int,float)):
#          res*=i
# print(res)







