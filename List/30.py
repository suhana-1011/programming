'''Flattening a 2D List'''
# l1=[1,2,[3,4,5],6,[7,8]]
# res=[]
# for i in l1:
#     if type(i)==list:
#         for j in i:
#             res.append(j)
#     else:
#         res.append(i)
# print(res)

'''another without using j loop'''
# l1=[1,2,[3,4,5],6,[7,[8]]]
# res=[]
# for i in l1:
#     if type(i)==list:
#         res.extend(i)
#     else:
#         res.append(i)
# print(res)

'''recurrsion'''
# l=[0,1,2,3,4,3,2,1,0]
# for i in range(5):
#     print(i,end='')
# for i in range(3,-1,-1):
#     print(i,end='')


'''recurrsion without for loop'''
# def fun(n):
#     if n<4:
#         print(n,end='')
#         fun(n+1)
#     print(n,end='')
# print('start')
# fun(0)
# print('\nend')

'''using range of'''
# def fun(start,stop):
#     if start<stop:
#         print(start,end='')
#         fun(start+1,stop)
# fun(0,10)

'''recurrsion using factorial'''
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(5))



#decimal-binary
# binary-decimal
# sum 1-n using recurrsion


'''Flattening a 2D List using recurrsion'''
def flatten(l):
    res=[]
    for i in l:
        if type(i)==list:
            res+=flatten(i)
        else:
            res.append(i)
    return res
l1=[1,2,[3,4,5],6,[7,8]]
print(flatten(l1))


    

    
