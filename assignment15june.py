#assignment8

#question1
r=int(input("enter the radius:"))
class Circle:
     def getArea(self,r):
        area=3.14*r*r
        print("area of the circle is: %.2f" %(area))


     def getCircumfrence(self,r):
        circum=2*3.14*r
        print("circumfrence of the circle is: %.2f"%(circum))

f=Circle()
f.getArea(r)
f.getCircumfrence(r)

#question2
name=input("enter your name")
rollno=int(input("enter  roll.number"))
class Student:
    def display(self,name,rollno):
        print(name)
        print(rollno)
h=Student()
h.display(name,rollno)

#question3
faren=float(input("enter the fahrenheit:"))
cels=float(input("enter the celsius:"))
class Temperature:
    def convertFahrenheit(self,cels):
        cl=cels*9/5+32
        print("conversion of celsius to fahrenheit is: %.2f"%(cl))

    def convertCelsius(self,faren):
        fr=(faren-32)*1.8
        print("conversion of fahrenheit to celsius is:: %.2f"%(fr))
x=Temperature()
x.convertFahrenheit(cels)
x.convertCelsius(faren)


#question4
movie=input("Enter the movie")
artist=input("Enter artist's name")
year=input("Enter Year of release")
rate=int(input("Enter ratings"))

class MovieDetails :
    def displaydetails(self,movie,artist,year,rate):
        print("movie"+movie)
        print("Artist name" + artist)
        print("Year of release" + year)
        print("ratings %d"%(rate))
    def updatedetails(self,movie,artist,year,rate):
        movie = input("Enter movie ")
        artist = input("Enter artist's name-" )
        year = input("Enter the Year of release- ")
        rate = int(input("Enter ratings-"))

        print("The new movie is-" + movie)
        print("The new artist's name is-" + artist)
        print("The new Year of release is-" + year)
        print("The new ratings%d" % (rate))

a=MovieDetails()
a.displaydetails(movie,artist,year,rate)
a.updatedetails(movie,artist,year,rate)

 #question5
class Expenditure:

    def displayresult(self, expen,save):

        print("Expenditure %d"%(expen))

        print("Saving"
              "s %d"%(save))

        print("")

    def calculateresult(self, expen,save):

        salary=expen+save

        return salary
    def displaysalary(self,sal):

        print("Total salary %d" % (sal))



expen = int(input("Enter expenditure"))

save = int(input("Enter savings"))

e = Expenditure()

e.displayresult(expen,save)

e.calculateresult(expen,save)

sal=e.calculateresult(expen,save)
e.displaysalary(sal)





