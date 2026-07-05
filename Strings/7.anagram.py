#WAP to check the given strings are anagram strings or not
def bubble_sort(s1):
    l1=list(s1)
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if l1[i]>l1[j]:
                l1[i],l1[j]=l1[j],l1[i]
    return "".join(l1)
s1='silent'
s2='listen'

#s1='the classroom
#s2='school master
if bubble_sort(s1)==bubble_sort(s2):
    print("Anagram Strings")
else:
    print("Not Anagram Strings")
