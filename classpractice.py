class Bird:
    def __init__(self,color,breed): #Constructor
        self.color=color
        self.breed=breed
    def speak(self):                # for each method, self parms is mandatory
        print("asdfasdfadf")
    def details(self):
        print(self.color,self.breed)

par=Bird("par","asdfasdf")          #constructor instantiation
par.details()
par.speak()

