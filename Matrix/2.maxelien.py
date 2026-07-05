'''maxelien'''
row=int(input('Enter row: '))
col=int(input('Enter col: '))
matrix1=[[int(input('Enter values: '))for col in range(col)]for row in range(row)]
print('Matrix1')
for i in range(row):
    for j in range(col):
        print(matrix1[i][j],end=" ")
    print()

m=matrix1[0][0]
for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        if matrix1[i][j]>m:
           m=matrix1[i][j]
print('Maximum element in given matrix is: ',m)


#SUM of each row and sum of each col
row=int(input('Enter row: '))
col=int(input('Enter col: '))
matrix1=[[int(input('Enter values: '))for col in range(col)]for row in range(row)]
print('Matrix1')
for i in range(row):
    for j in range(col):
        print(matrix1[i][j],end=" ")
    print()

for i in range(len(matrix1)):
    row_sum=0
    for j in range(len(matrix1)):
        row_sum+=matrix1[i][j]
    print(row_sum)

for i in range(len(matrix1)):
    col_sum=0
    for j in range(len(matrix1)):
        col_sum+=matrix1[j][i]
    print(col_sum)
    