class Bird():
    def intr(self):
        print("There are many bird in world ")
    def Flight(self):
        print("There are many bird Some bird are fly and some are not ")
class Sparrow(Bird):
    def Flight(self):
        print("Sparrow are fly")
    
class ostrich(Bird):
    def Flight(self):
        print("ostrich cannot not fly")
        
Obj_bird=Bird()
Obj_bird.intr()
Obj_bird.Flight()

Obj_Spp=Sparrow()
Obj_Spp.Flight()
Obj_Spp.intr()

Obj_OST=ostrich()
Obj_OST.Flight()
Obj_OST.intr()

        