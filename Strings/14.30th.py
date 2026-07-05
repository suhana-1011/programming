#WAP to encode a given str as folows based on shift value:
#s1='Hide the dead body'
#shift=4
#dont give space after chr
#at last while iterating 'y' , it should be converted to letter only, start from a(coz 121+4=spl char)
s1 = 'Hide the dead body'
shift = 4
result = ''
for ch in s1:
    if ch.isupper():
        result += chr((ord(ch) - 65 + shift) % 26 + 65)
    elif ch.islower():
        result += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        result += ch  # keep space/other chars as is, no shifting

print(result)


#Count the no. of special characters in each word, if count is even reverse(in same place),if odd place as it is
s1='I@@! am!@$! pool!!@#$$ Deadpool!@ Here%^#@! to!@ kill!@# Bad!@#$ guys!@@#$@#!'
s2 =s1.split()
print(s2)
s3 = ""
for i in s2:
    cnt=0
    for j in i:
        if ord(j)>=65 and ord(j)<=90 or ord(j)>=97 and ord(j)<=122:
            continue
        else:
            cnt+=1
    #print(i,"->",cnt)
    if cnt%2==0:
        s3+=i[::-1]+" "
    else:
        s3+=i+" "
print(s3)

#Display the count of substring present in a original string
s1='abcabcbbbccabcdabcbbbdab'
s2='abc'
count=0
for i in range(len(s1)):
    if s1[i:i+len(s2)]==s2:
        count+=1
print(count)

#Display the key and value pair of unique word along with its count of vowels and consonants in the form of list
s1='Once the most violent man called one man the most violent'
s2=s1.split()
for i in s2:
    v,c=0,0
    letter=i
    for j in letter:
        if j in 'aeiouAEIOU':
            v+=1
        else:
            c+=1
    print(letter,':','[',v,',',c,']')

#d1={}
#for i in s1.split():
#v,c=0,0
#for j in i:
#if j in 'aeiouAEIOU':
# v+=1
# else:
# c+=1
# if i not in d1:
#d1[i]=v,c
#for k,v in d1.items():
#print(k,":",v)

#WAP to encode given str based on the shift value
s1='Ironman'
shift = int(input('Shift Value: '))
s2=''
for i in s1:
    s2+=chr(ord(i)+shift)
print(s2)

# #WAP to group the anagrams from the given input list
# def string_sorting(s):
#     l1=list(s)
#     for i in range(len(l1)):
#         for j in range(i+1,len(l1)):
#               if l1[i]>l1[j]:
#                 l1[i],l1[j]=l1[j],l1[i]
#     return "".join(l1)
# d1 = {}
# s1=['ate','tan','tea','eat','nat','bat','tab']
# for i in s1:
#     res = string_sorting(i)
#     if res not in d1:
#         d1[i]=[i]
#     d1[i].append(i)
# print(d1)
#have to complete it yet

#WAP to group the anagrams from the given input list
def string_sorting(s):
    l1 = list(s)
    for i in range(len(l1)):
        for j in range(i+1, len(l1)):
            if l1[i] > l1[j]:
                l1[i], l1[j] = l1[j], l1[i]
    return "".join(l1)

d1 = {}
s1 = ['ate', 'tan', 'tea', 'eat', 'nat', 'bat', 'tab']

for i in s1:
    res = string_sorting(i)
    if res not in d1:
        d1[res] = [i]
    else:
        d1[res].append(i)

print(d1)


       

