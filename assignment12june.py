#ques1
i=0
while(i<10):
    num=input("enter the age")
    print(num)
    i=i+1

#ques2
while(True):
    print("infinite")
 #will lead to infinity

#ques3
num=[]
for a in range(0,5):
    x=int(input("enter your number"))
    num.append(x)
print(num)
sq=[]
for a in num:
    val=a*a
    sq.append(val)
print(sq)

#ques4
x=['xyz',2.5,30,22.5,1,'yeah','baby']
i=0
list1=[]
list2=[]
s_t=[]
y=[]

list1 = [y for y in x if type(y) == int]
list2 = [y for y in x if type(y) == float]
s_t = [y for y in x if type(y) == str]

print(list1)
print(list2)
print(s_t)


#question5
odd=[]
even=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)

#question6
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()


#question7
d={'name':'xyz','age':21,'city':'jalandhar'}
for i in d:
    print(d[i])
print(dict.keys(d))
print(dict.items(d))

#question8
a=[]
i=0
while i<=4:
   num=int(input("ENTER THE VALUE"))
   a.append(num)
   i+=1

print(a)
i=0

s=int(input("ENTER THE VALUE YOU WANT TO DELETE"))
if s in a:
    a.remove(s)
    print("ElEMENT REMOVED!")
else:
    print("ELEMENT NOT FOUND")
print(a)