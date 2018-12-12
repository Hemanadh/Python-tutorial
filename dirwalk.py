import os
for (dirname, subdir, files) in os.walk('C:\\Users\\ABRIDGE0\\Desktop'):
        for myfile in files:
                filename=os.path.join(dirname,myfile)
                size=int(os.path.getsize(filename))/1024
                extFilename=filename.split("/")
                if size>5:
                    print("filename: {} --> size : {} MB ".format(,size))
			
