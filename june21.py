#exception_handling
try:
    a=int(input("enter no:"))
    print(a)
    b=10/a
    print(b)
except ValueError:
    print("enter only integer")
except ZeroDivisionError:
    print("number divided by zero")


#for
#exceptvalue(ValueError,ZeroDivisionError)
finally:
    print("will execute whether exceptions occurs or not")

#indexError
try:
    a=[1,3,4]
    print(a[2])


except IndexError:
    print("limit exceeded")


#importError
try:
    import asddfggh
    print("qwerty")

except ImportError:
    print("file not found")

#
try:
    age=int(input("enter age"))
    if(age(18))