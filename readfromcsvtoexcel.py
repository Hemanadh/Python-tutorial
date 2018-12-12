import xlwt
wb=xlwt.Workbook();
syf=wb.add_sheet("StudentDetails");
f=open('marks.csv','r')
row=0
for line in f:
    values=line.split(',')
    Col=0
    while Col<len(values):
        syf.write(row,Col,values[Col])
        Col+=1
    row+=1
wb.save("marksexcel23.xls")
f.close()
