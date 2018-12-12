import re

inputStr = "Aaa keljert12234"

# search function

if re.search('B',inputStr):
    print("true")
else:
    print("false")


# match function

if re.match('A',inputStr):
    print("true")
else:
    print("false")
    
# match function with ignore case

if re.match('A',inputStr,re.IGNORECASE):
    print("true")
else:
    print("false")

#contains the word

if re.search('[kelr]',inputStr,re.IGNORECASE):
    print("true")
else:
    print("false")

#Numeric [0-9] , \d

if re.search('[0-9]',inputStr,re.IGNORECASE):
    print("true")
else:
    print("false")

#not starting with smaller case
#    ^[^a-z]

#Quantifiers [10 digit number] \d{10}
input="7777esdedrtgesrt88888"
if re.search('\d{6}',inputStr,re.IGNORECASE):
    print("Quan -> true")
else:
    print("Quan -> false")


#Quantifiers [10 digit number] \d{10}
input="7777esdedrtgesrt88888"
if re.search('\d{6}',inputStr,re.IGNORECASE):
    print("Quan ->true")
else:
    print("Quan ->false")

    
#.. 
input="edwerwerr"
if re.search('e.r',input,re.IGNORECASE):
    print("..... _>true")
else:
    print("false")

#.. 
input11="aedqweedrqweqwe"
if re.search('q.?e',input11,re.IGNORECASE):
    print("..... _>true")
else:
    print("false")

# split
input11="hemanadh-vadamala@gmail.com"
print(re.split("[-:@]",input11))

#substitute
input12="11111asdfasdfadfasdfadsf11111jlkhlhl22222"
print(re.sub('\d','*',input12))
print(re.sub('\d+','*',input12))    

#re.group()
#re.span()
