#Accetp 2 dtrings and mix the 2 strings as follows
s1='abcd'
s2='wxyz'
s3=''
for i in range(len(s1)):   
    s3+=s1[i]+s2[len(s2)-1-i]
print(s3)
