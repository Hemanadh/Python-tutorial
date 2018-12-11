import random
n=random.randint(1,100)
g=int(input("Enter number : "))
for x in range(3):
    if g>n:
        print("Enter Smaller num:")
    elif g<n:
        print("Enter Bigger num:")
    else:
        print("Congo !")
        break
    g=int(input("Enter number : "))
