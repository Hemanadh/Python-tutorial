import xlrd
import xlwt
wb = xlrd.open_workbook("C:\\Users\\ABRIDGE0\\Desktop\\DAY2\\titanic3.xls") #Open Workbook
print(wb.nsheets)       #print no of Sheets
print(wb.sheet_names()) # Print sheet names

ws = wb.sheet_by_name('titanic3')  # open sheet

print(ws.nrows) #print no of columns
print(ws.ncols) #print no of columns

wb=xlwt.Workbook();

syf=wb.add_sheet("SYF");

syf.write(0,0,"Passenger Name")


for x in range(10):
    print(ws.cell(x,2).value)
    syf.write(x+1,0,ws.cell(x,2).value)

wb.save("PassengerNames.xls")
