def gcd(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=gcd(a,b)
print("The GCD of two Numbers is: ",c)