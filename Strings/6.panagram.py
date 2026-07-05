#WAP to check the given strings are panagram strings or not
#All the alphabets should be present
s1='The Quick brown fox jumps over a lazy dog'
#s1='Pack my box with five dozen liquor jugs'
#s1='Patience is my strongest suit'
s2=set()
for i in s1:
    if i==' ':
        continue
    else:
        s2.add(i.lower())

if len(s2)==26:
    print("Panagram string")
else:
    print("Not a Panagram string")