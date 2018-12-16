a=int(input("Enter the year: "))
def leap(y):
    return y % 4 == 0 and (y % 400 == 0 or y % 100 != 0)
print(leap(a))


