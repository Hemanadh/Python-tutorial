class Dog:
    def __init__(self,color,breed):
        self.color=color
        self.breed=breed
    def speak(self):
        print("bhou..bhou")
    def wish(self,name):
        print("hello, " + name)
    def hi(self):
        print("I am a {} colored {}".format(self.color,self.breed))

tommy = Dog("yellow","lab")
tommy.speak()
tommy.wish("bhaskar")
print(tommy.color)
print(tommy.breed)


print(type(tommy))
print(isinstance(tommy,Dog))

tommy.hi()
