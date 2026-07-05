#WAP to display the frequency of each character in the given string
s1='Supercalifragilisticexpalodicious'
d1={}
for i in s1:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1
print(d1)
for k,v in d1.items():
    print(k,v)
    