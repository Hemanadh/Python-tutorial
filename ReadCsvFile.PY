
f=open('marks.csv','r')

for x in f:
    lines=x.split(',')
    marks=int(lines[1])+int(lines[2])+int(lines[3])
    print("Student Name : {}, Avg marks: {}".format(lines[0],marks/3))
    
f.close()
