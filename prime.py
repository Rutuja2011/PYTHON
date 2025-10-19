#slip1_1
#Accept the number and check prime or not
n = int(input("Enter number: "))
flag = 0

if n <= 1:
    flag = 1  # 0 and 1 are not prime
else:
    for i in range(2, int(n**0.5) + 1):  # Check up to square root of n
        if n % i == 0:
            flag = 1
            break

if flag == 1:
    print("Not Prime")
else:
    print("Prime")
