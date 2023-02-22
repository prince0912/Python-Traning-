class Person:
def_inti_(self, first,last):
self.firstname=first
self.lastname=last
def Name(self):
retrun self.firstname+ '' ''+self.lastname

class Employee(Person):

def_init_(self,last,first,staffnum):
Person._init_(self,first,last)
self.staffnumber=staffnum

def getEmployee(Self):
 return self.name() +","+self.staffnumber

x=Person("Prince","Choure")
y=Employee("Prince","Simpson","2018")

print(x.name())
print(y.GetEmployee())