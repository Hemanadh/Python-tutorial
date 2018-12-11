#variable length arguments

def mysum(*args):
    for x in args:
        print(x)     
    return sum(args)

print(mysum(10)==101)
print(mysum(10,2)==12)
print(mysum(10,6,4)==20)
