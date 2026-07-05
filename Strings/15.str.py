#WAP to Display the first non-repeating character along with its index
def first_non_repeating_char(s1):
    for i in range(len(s1)):
        count=0
        for j in range(len(s1)):
            if s1[i]==s1[j]:
                count+=1
        if count==1:
            return s1[i],i
    return -1
#print(first_non_repeating_char('programming'))
print(first_non_repeating_char('swiss'))
#print(first_non_repeating_char('aaa'))
#print(first_non_repeating_char(''))
      

    #Insert the second str in the middle of first string
# s1='Dhoni'
# s2='Sakshi'
# s3=''
# mid=(0+len(s1)-1)/2
# s1.split(mid)
# for i in s1:
#     s3=s1+s2+mid+s1
# print(s3)
#have to complete it yet

#Insert the second str in the middle of first string
s1 = 'Dhoni'
s2 = 'Sakshi'

mid = len(s1) // 2

first_half = s1[:mid]
second_half = s1[mid:]

s3 = first_half + s2 + second_half
print(s3)

#WAP to display the longest word in a given sentence
def longest_word(s1):
    s2=s1.split()
    longest=''
    for word in s2:
        if len(word)>len(longest):
            longest=word
    return longest,len(longest)


s1='always do good to others it will come back in unexpected ways'
#s1='aa bb'
print(longest_word(s1))

#the given str can be a mirror str or not
# def is_mirror(s1):
#     pass
#     mirror_chars={'A','H','I','M','O','T','U','V','W','X','Y','o','v','w','x','0','8'}
#     for i in s1:
#         if i not in mirror_chars:
#             return False
#     return True
# s1='AHA'
# if is_mirror(s1):
#     print('Mirror String')
# else:
#     print('Not a mirror string')
#handle 'HIM and "TIH" as they'll be shown as mirror str

#the given str can be a mirror str or not
def is_mirror(s1):
    mirror_chars = {'A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'o', 'v', 'w', 'x', '0', '8'}

    # Step 1: every character must individually be a mirror-symmetric character
    for i in s1:
        if i not in mirror_chars:
            return False

    # Step 2: the string itself must read the same when reversed
    # (this catches cases like 'HIM' or 'TIH' where each char is
    # individually mirror-symmetric, but the whole string isn't,
    # since mirroring flips the order left-to-right too)
    if s1 != s1[::-1]:
        return False

    return True

s1 = 'AHA'
if is_mirror(s1):
    print('Mirror String')
else:
    print('Not a mirror string')

#WAP to check the given str can become a strong password or not
Password='Ammarah_d6'
if len(Password)>=8 and len(Password)<=30:
    uc,lc,nc,sc=0,0,0,0
    for i in Password:
        if ord(i)>=65 and ord(i)<=90:
            uc+=1
        elif ord(i)>=97 and ord(i)<=122:
            lc+=1
        elif ord(i)>=48 and ord(i)<=67:
            nc+=1
        else:
            sc+=1
    if uc>=1 and lc>=1 and nc>=1 and sc>=1:
        print('Strong Password')
    else:
        print('Weak Password')
else:
    print('Password must be of atleast 8 characters')
    