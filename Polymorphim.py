class India():
    def Capital(self):
        print("New Dehli is Capital of india")
    def Currency(self):
        print("Rupee is India Currency ")
    def Continents(self):
        print("India in Asia Continents ")
class USA():
    def Capital(self):
        print("Washingtan D C is capital of USA")
    def Currency(self):
        print("Doller is Currency of USA")
    def Continents(self):
        print("USA is in North America")
obj_ind = India()
obj_Usa = USA()
for country in (obj_ind,obj_Usa):
    country.Capital()
    country.Continents()
    country.Currency()