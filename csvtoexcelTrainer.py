import xlwt
f  = open("marks.csv","r")
wb = xlwt.Workbook()
ws = wb.add_sheet("marks")
for row,line in enumerate(f):
    for col,data in enumerate(line.strip().split(",")):
        ws.write(row,col,data)
        #print(row,col,data)

wb.save("marks.xls")
