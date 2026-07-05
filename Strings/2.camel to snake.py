#WAP to convert the given camel case str to snake case str
s1='If You Are Good At Something Never Do It For Free'
s2=''
print(s1)
for i in s1:
    if i==' ':
        s2+='_'
    elif ord(i)>=65 and ord(i)<=90:
        s2+=chr(ord(i)+32)
    elif ord(i)>=97 and ord(i)<=122:
        s2+=chr(ord(i))
print(s2)