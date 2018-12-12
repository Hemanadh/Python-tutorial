class Dog:
    color=""
    breed=""
    def speak(self):
        print("bhou..bhou")
    def wish(self,name):
        print("hello, " + name)
    def hi(self):
        print("I am a {} colored {}".format(self.color,self.breed))

tommy = Dog()
tommy.speak()
tommy.wish("bhaskar")
tommy.color=123;
tommy.breed="asadad";
print(tommy.color)



print(type(tommy))
#print(isinstance(tommy,Dog))

tommy.hi()
