class Father:
    
    def father_quality(self):
        print("inside father class")
        print("father was a honest man")
        print()
class Mother:
    
    def mother_quality(self):
        print("inside mother class")
        print("mother is innocent")
        print()
class Son(Father,Mother):
    def son_quality(self):
        print("inside son class")
        print("son was a good boy")
        print()

dad = Father()
mom = Mother()
son = Son()
son.father_quality()
son.mother_quality()
son.son_quality()
