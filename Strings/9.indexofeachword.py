s1='If you always do what you always did you will always get what you always got'
s2=s1.split()
d1={}
for i in range(len(s2)):
    if s2[i] not in d1:
        d1[s2[i]]=[i]
    else:
        d1[s2[i]]+=[i]
print(d1)

    