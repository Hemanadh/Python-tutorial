class Baby:
    def __init__(self,name): #Constructor
        self.name=name
    def cry(self):                # for each method, self parms is mandatory
        print("crying")
    def laugh(self):
        print("Laughing")
    def hi(self):
        print("Hello, I am",self.name)        

