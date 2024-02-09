class Bird():
    def intro(self):
        print("there are many types of birds")
    def flight(self):
        print("Many of them fly and many cannot")
class Sparrow(Bird):
    
    def flight(self):
        print("Sparrows can fly")
class Ostrich(Bird):
    
    def flight(self):
        print("ostrich cannot fly")
bird_obj = Bird()
sparrow_obj = Sparrow()
ostrich_obj = Ostrich()

sparrow_obj.intro()
sparrow_obj.flight()
ostrich_obj.intro()
ostrich_obj.flight()



