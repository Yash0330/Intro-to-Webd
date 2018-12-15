print("Enter the Number:  ")
n=int(input())
f=[1,1]

if n<0 :
    print("invalid")
elif n==1 :
    print("1\n1")
elif n==0 :
    print(f[0])
else:
    print("0\n1\n1")
    for i in range(2,n+1) :

        t=f[i-1]+f[i-2]
        f.append(t)
        print(t)
