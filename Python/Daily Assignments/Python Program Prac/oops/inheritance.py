class Parent():
    def __init__(self,name,number):
        self.name = name
        self.number = number
    def display(self):
        print("parent class",self.name)
        print("parent class",self.number)
    def details(self):
        print(self.name)
        print(self.number)
class Employee(Parent):
    def __init__(self, name, number,salary,post):
        self.salary = salary
        self.post = post
        
    #invoking parent class constructor in child class
    
        Parent.__init__(self,name,number)
    
    def details(self):
        print("child class",self.name)
        print("child class",self.salary)
        print("child class",self.post)

obj1 = Employee("abhi",580,25000,"Business analyst")
obj1.display()
obj1.details()