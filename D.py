from datetime import datetime
import time
d=datetime.now()
print (d)
print (d.year)
print (d.month)
print (d.day)
print (d.hour)
print (d.minute)
print (d.second)

print(d.strftime('%A %d. %B %Y'))
print(d.strftime('%d/%m/%y'))

a=datetime.today()
b=datetime(1947,8,15)

print((a-b).days)

#performance measurement

starttime=time.time()

for x in range(10000):
	x**x

endtime=time.time()

print(endtime-starttime)

time.sleep(1)
