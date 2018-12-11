
def grep(file,pattern):
    f=open(file,"r")
    for index,line in enumerate(f):
        if pattern in line:
            print(line.rstrip(),index)
   
    f.close()

grep("fileinput1.txt","sdf")

