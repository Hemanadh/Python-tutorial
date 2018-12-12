import os
import zipfile
import glob

sourceDir ="C:\\Users\\ABRIDGE0\\Desktop\\DAY1"
pattern="*.py"
destDir="C:\\Users\\ABRIDGE0\\Desktop\\DAY1\\syf.zip"
os.chdir(sourceDir)
fileList=glob.glob(pattern)
z=zipfile.ZipFile(destDir,"w",zipfile.ZIP_DEFLATED)
for file in fileList:
    z.write(file)

z.close

                
