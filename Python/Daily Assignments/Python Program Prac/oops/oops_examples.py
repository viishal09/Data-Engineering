class Bird:
    def __init__(self,name):
        self.name = name
        
    def intro(self):
        print("the bird is:",self.name)
        
    def fly(self):
        print("bird can fly")
class Parrot(Bird):
    
    def __init__(self,name,color,character):
        super().__init__(name)
        self.color = color
        self.character = character
    #method over riding
    def intro(self):
        print("the bird name is:",self.name)
        print("the bird color is:",self.color)
        print("the bird character is:",self.character)

        
bird_obj = Parrot('paroot','red','good')
bird_obj.fly()
bird_obj.intro()