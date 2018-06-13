#functions
def hello():
    print("hello")
    return 0
hello()

def add(a,b):
    return a+b
print(add(2,3)) #call by value

def add(a,b):
    return a+b
print(add(b=2,a=3)) #call by refrence


a=2 #global scope

def add(a):
    a=3  #static scope
    print(a)

add(a)

a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
def sub(a,b=5):
    return a-b
print(sub(a,b))
