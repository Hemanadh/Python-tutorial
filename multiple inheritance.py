class Dog:
    name="sdf"
    def speak(self) :print("bhou..bhou")
    def guard(self) :print("I am guarding your home")

class Cat:
    name1="rdf"
    def speak(self) :print("meau..meau")
    def hunt(self)  :print("I am hunting mice")

class Doat(Cat,Dog):
    def speak(self):
        print("bhou..meau")
    def pspeak(self):
        super().speak()
        
#Object instanciation
ginger = Doat()

ginger.hunt()
ginger.guard()
ginger.speak()
ginger.pspeak()
print(ginger.name)
