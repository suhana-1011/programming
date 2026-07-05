s1='Python coding is awesome'
c=0
v=0
for i in s1:
    if i==' ':
        continue
    elif i in 'aeiouAEIOU':
        v+=1
    else:
        c+=1
print('Vowels count: ',v)
print('Consonant count: ',c)