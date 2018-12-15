def comma(n):
    if len(n) < 4:
        return n
    else:
        return comma (n[:-3]) + ',' + n[-3:]
a=input("Enter the Number: ")
print(comma(a))

