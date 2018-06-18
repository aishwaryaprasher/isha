#ques1
class Animal:
    def animal_attribute(self):
        print('Animals belong to Phylum kingdom')

class Tiger(Animal):
    def tiger_attribute(self):
        print('Tiger is an animal')
        print("")

animal = Tiger()
animal.animal_attribute()
animal.tiger_attribute()

#ques2
#print a.f(), b.f()- answer is AB
#print a.g(), b.g()-answer is AB

#ques3
class Cop:
    def __init__(self,name,age,workexp,desg):
        self.name=name
        self.age=age
        self.workexp = workexp
        self.desg = desg


    def add(cls):
        cls.name=input("Enter name")
        cls.age=int(input("Enter age"))
        cls.workexp=int(input("Enter work experience"))
        cls.desg=input("Enter the designation")
        return Cop(cls.name,cls.age,cls.workexp,cls.desg)


    def display(cls):
        print("Details of employee-")
        print("Name- "+cls.name)
        print("Age- %d"%cls.age)
        print("Work experience- %d" %cls.workexp)
        print("Designation-->"+cls.desg)

    def update(self):
        print("Update details-")
        self.add()
        self.display()

obj1=Cop("xyz",21,9,"SP")
obj1.add()
obj1.display()
obj1.update()

#ques4
class Shape:
    def __init(self,len,bre):
        self.len=len
        self.bre=bre
class Square(Shape):
    def area(self,len):
        return len*len
class Reactangle(Shape):
    def area(self,len,bre):
        return len*bre

obj=Shape()
obj1=Square()
obj2=Reactangle()
len=int(input("Enter the length"))
bre=int(input("Enter the breadth"))
print(obj1.area(len))
print(obj2.area(len,bre))