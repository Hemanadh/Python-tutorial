def function(string,character):
    listOfOps=[]
    count=0
    for x in string:    
        if x == character:            
            listOfOps.append(count)
        count+=1
    return listOfOps    
print(function("ciscosdfdcsedfchfghfc","c"))


#---------------------------------------------


def function(string,character):
    listOfOps=[]
    for index,mychr in enumerate(string):    
        if mychr == character:            
            listOfOps.append(index)      
    return listOfOps    
print(function("ciscosdfdcsedfchfghfc","c"))
     
