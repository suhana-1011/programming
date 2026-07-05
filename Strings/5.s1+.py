s1='Ammarah'
n=len(s1)
if n%2!=0:
    for i in range(n):
        for j in range(n):
            if i==n//2:
                print(s1[j],end=" ")
            elif j==n//2:
                print(s1[i],end=" ")
            else:
                print(" ",end=" ")
        print()
else:
    print('It will not work for even values')


