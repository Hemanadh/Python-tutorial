import sys
filename=sys.argv[1];
pattern=sys.argv[2];
f=open(filename,"r")
for index,line in enumerate(f):
    if pattern in line:
        print(line.rstrip(),index)
f.close()

