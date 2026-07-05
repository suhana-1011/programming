n = int(input("enter a number: "))

for val in range(2, n+1):
    count = 0

    for i in range(2, val//2 + 1):
        if val % i == 0:
            count += 1
            break

    if count == 0:
        print(val, end=" ")
        