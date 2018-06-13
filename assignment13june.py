#assignment7
#ques1
r=int(input("enter the radius"))
ans=0
def rad(r):
    ans=22.7*r*r
    return ans
print(rad(r))

#ques2
i=0
sum=0
def perft():
    for i in range(1,1000):
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum=sum+j;

        if sum==i:
            print("%d"%(i))
    return 0
print("perfect no ")
perft()


#Ques3
l=int(input("Enter the limit"))
def table(l):
     if l==1:
         answer=12*1
         return print(answer)
     else:
         table(l-1)
         answer= ("12*%d=%d"%(l,(12*l)))
         print("")
         return print(answer)
print("TABLE OF 12")
print(table(l))


#Ques4

result=1
a=int(input("Enter number"))
b=int(input("Enter power"))

def power(a,b):
    if b!=0:
        return (a*power(a,b-1))
    else:
        return 1
result=power(a,b)
print("Answer =%d"%(result))


#Ques5

n=int(input("Enter limit"))
def fac(n):
    if n==1:
       return 1
    else :
        return (n*fac(n - 1))

dict={'number':n,'Factorial':fac(n)}
print(fac(n))
print(dict)




