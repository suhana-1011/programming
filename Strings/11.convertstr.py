#WAP to convert the given string based on below conditions:
#1. If the length of str is even, convert even number ASCII character to @ and space to #
#2. If the length of str is odd, convert odd number ASCII character value to $ and space to ^
s1='I Love programming in python'
res = ''
count = 0
for i in s1:
    if i == ' ':
        continue
    else:
        count+=1
print(count)
if count%2==0:
    for i in s1:
        if i == ' ':
             res+='#'
        else:
            if ord(i)%2==0:
                res+='@'
            else:
                res+=i
else:
    for i in s1:
        if i == ' ':
            res+='^'
        else:
            if ord(i)%2!=0:
                res+='$'
            else:
                res+=i
print(res)
