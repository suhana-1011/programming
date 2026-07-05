s1='Ammarah'
j=len(s1)-1
for i in range(len(s1)):
    if s1[i]!=s1[j]:
        print("Not a Palindrome")
        break
    j=j-1
else:
    print("Palindrome")
