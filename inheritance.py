from baby import Baby
class Toddler(Baby):
    def sleep(self):
        print("la..la..laa")
    def cry(self):
        print("only folks in serials cry")
class Toddler2(Baby):
    def sleep(self):
        print("la..la..laa 2")
    def cry(self):
        print("only folks in serials cry 2")        

pinky=Toddler("Haritha")
buckey=Toddler2("Bucey")

pinky.laugh()
pinky.sleep()
pinky.cry()
print(pinky.name)


buckey.laugh()
buckey.sleep()
