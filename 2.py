n=55
g=int(input("Enter number : "))
while True:
    if g>n:
        print("Enter Smaller num:")
    elif g<n:
        print("Enter Bigger num:")
    else:
        print("Congo !")
        break
    g=int(input("Enter number : "))
