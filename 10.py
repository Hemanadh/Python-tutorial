#dictionaries
fate = {"TG":"TRS"
        ,"Chattisgarh":"Congress"
        ,"MP":"BJP"
        ,"RJ":"Congress"
        }

print(len(fate))

#read
print(fate["TG"])
print(fate.get("TG"))
#add
fate["AP"]="BJP"
print(len(fate))
print(fate.get("AP"))
#update
fate["AP"]="TDP"
print(fate.get("AP"))
#delete
del fate["AP"]
print(len(fate))

#Place Holders
for x in fate:
    print("{}----->>{}".format(x,fate[x]))

for x in fate:
    print("{1}----->>{0}".format(x,fate[x]))



for x,y in fate.items():
    print(x+"->"+y)
    
