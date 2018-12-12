import xlwt

wb=xlwt.Workbook();

syf=wb.add_sheet("SYF");

syf.write(0,0,"Name")
syf.write(1,0,"Hemanadh")

wb.save("Hello.xls")
