for i in range(int(input())) :
    a=input("Enter the word: ")
    print("The abbreviation is: ",end="")
    print (''.join(e[0] for e in a.split()))
