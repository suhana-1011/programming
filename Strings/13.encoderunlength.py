#WAP to encode a run length of a string
s1='aaaaaabbccccccdddeeefffffgggh'
#o/p: a6b2c6d3e3f5g3h1
s2=''
count = 1 #If count=0 main result will be res-1
for i in range(len(s1)-1): #range(len(s1)-1) if from 0 to n-1
    if s1[i]==s1[i+1]:
        count+=1
    else:
        s2+=s1[i]+str(count)
        count=1
s2+=s1[-1]+str(count)
print(s2)

#aaaaaabbccccccdddeeefffffggghhaaacccdd
#Already present letters should have count at first 
#Insert the second str in the middle of first string