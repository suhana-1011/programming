#WAP to divide the string based on integer value when we follow the given conditions
#-. Remove all the spaces
#-. Count the total length
#-. Based on count find its square root and divide the chars
import math
s1='Everything is fair in love and war'
s2=''
for i in s1:
    if i==' ':
        continue
    else:
        s1+=i
cnt = round(math.sqrt(len(s2)))
s3=''
val=0
for i in s2:
    if cnt ==val:
        s3+='\n'
        val=0
    val+=1
    s3+=i
print(s3)
