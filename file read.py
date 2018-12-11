

f=open("fileinput.txt","r")
totalSize=0
for line in f:
    listOfFields=line.split();
    data=listOfFields[-1]
    totalSize+=int(data);
f.close()
print("Size in KB : {}".format(totalSize))
print("Size in MB : {}".format(round(totalSize/1024)))
print("Size in GB : {}".format(round((totalSize/1024)/1024,1)))

 

