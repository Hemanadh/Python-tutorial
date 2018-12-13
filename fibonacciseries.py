#fibonacci series
a,b=0,1
while a < 1000:
    print(a)
    a,b=b,a+b;
    
#-------------------------

    x=[0,1]
    for y in range(100):
        x.append(x[-1]+x[-2])

print(x)

