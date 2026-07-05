'''adddiagonal'''
row=int(input('Enter row: '))
col=int(input('Enter col: '))
matrix1=[[int(input('Enter values: '))for col in range(col)]for row in range(row)]
print('Matrix1')
for i in range(row):
    for j in range(col):
        print(matrix1[i][j],end=" ")
    print()

d1=0
d2=0
for i in range(row):
    for j in range(col):
        if i==j:
            d1+=matrix1[i][j]
        if i+j==row-1:
            d2+=matrix1[i][j]
print('Sum of first diag: ',d1)
print('Sum of second diag: ',d2)
print("Difference: ",abs(d1-d2))


'''
Enter row: 3
Enter col: 3
Enter values: 1
Enter values: 2
Enter values: 4
Enter values: 3
Enter values: 2
Enter values: 4
Enter values: 6
Enter values: 5
Enter values: 1
Matrix1
1 2 4 
3 2 4 
6 5 1 
Sum of first diag:  4
Sum of second diag:  12
Difference:  8
'''

'''matrixaddition'''
row=int(input('Enter row: '))
col=int(input('Enter col: '))
matrix1=[[int(input('Enter values: '))for col in range(col)]for row in range(row)]
print('Matrix1')
for i in range(row):
    for j in range(col):
        print(matrix1[i][j],end=" ")
    print()

matrix2=[[int(input('Enter values: '))for col in range(col)]for row in range(row)]
print('Matrix1')
for i in range(row):
    for j in range(col):
        print(matrix2[i][j],end=" ")
    print()

Result=[[0 for col in range(col)] for row in range(row)]

for i in range(row):
    for i in range(col):
        Result[i][j]=matrix1[i][j]+matrix2[i][j]
print('Result')

for i in range(row):
    for i in range(col):
        print(Result[i][j],end=" ")
    print()

'''matrix multiplication'''
row=int(input('Enter row: '))
col=int(input('Enter col: '))
matrix1=[[int(input('Enter values: '))for col in range(col)]for row in range(row)]
print('Matrix1')
for i in range(row):
    for j in range(col):
        print(matrix1[i][j],end=" ")
    print()

matrix2=[[int(input('Enter values: '))for col in range(col)]for row in range(row)]
print('Matrix1')
for i in range(row):
    for j in range(col):
        print(matrix2[i][j],end=" ")
    print()

result=[[0 for col in range(col)] for row in range(row)]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j]+=matrix1[i][k]*matrix2[k][j]
print('Result')

for i in range(row):
    for j in range(col):
        print(result[i][j],end=" ")
    print()