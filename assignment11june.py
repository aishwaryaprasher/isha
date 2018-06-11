#ques1
y=int(input("enter year"))
if(y%4==0):
    print("leap year")

else:
    print("not leap year")

#ques2
length=int(input("enter length"))
breadth=int(input("enter breadth"))
if(length==breadth):
    print("square")
else:
    print("reactangle")
#ques3
a=int(input("enter age of person1"))
b=int(input("enter age of person2"))
c=int(input("enter age of person3"))
if(a>b and a>c):
    print("a is greatest")
if(b>a and b>c):
    print("b is greatest")
if(c>a and c>b):
    print("c is greatest")
elif(a<b and a<c):
    print("a is youngest")
elif (b<a and b<c):
    print("b is youngest")
elif (c<a and c<b):
    print("c is youngest")
else:
 print("all ages are equal")

#question4
point=int(input("enter points"))
if point<200:
    if point>1 and point<=50:
        print("NO PRIZE WON")
    if point > 50 and point <= 150:
        print("CONGRATULATIONS YOU HAVE WON WOODEN DOG")
    if point > 151 and point <= 180:
        print("CONGRATULATIONS YOU HAVE WON BOOK")
    if point >180 and point <= 200:
        print("CONGRATULATIONS YOU HAVE WON CHOCLATES")

else:
    print("WRONG POINTS ENTERED")

#ques5
q=int(input("quantity is"))
p=q*100
if(p>1000):
    print("cost is% .2f "%(p-0.1*p))
else:
        print(p)
























































