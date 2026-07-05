s1='if_you_are_good_at_something_never_do_it_for_free'
s2=''
s2+=chr(ord(s1[0])-32)
print(s1)
for i in range(1,len(s1)):
    if s1[i]=='_':
        s2+=' '
    else:
        if s1[i-1]=='_':
            s2+=chr(ord(s1[i])-32)
        else:
            s2+=s1[i]
print(s2)