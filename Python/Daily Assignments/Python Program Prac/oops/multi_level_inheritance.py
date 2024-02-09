class Grandfather:
    def gf_quality(self):
        print("inside grand father class")
        print("grand father was a gentle man")
        print()
        
class Father(Grandfather):
    
    def father_quality(self):
        print("inside father class")
        print("father was a honest man")
        print()
class Son(Father):
    def son_quality(self):
        print("inside son class")
        print("son was a good boy")
        print()
gf = Grandfather()
Fath = Father()
son = Son()
son.gf_quality()
son.father_quality()
son.son_quality()
