#ques1
t=(1,2,5.65,'isha')
print(t)
t=len(t)
print(t)

#ques2
t=(2,3,4,5)
print(max(t))
print(min(t))

#ques3
t=(2*3*4)
print(t)

#sets
#ques1
a1=input("enter element1")
a2=input("enter element2")
a3=input("enter element3")


b1=input("enter element1")
b2=input("enter element2")
b3=input("enter element3")
set1=set([a1,a2,a3])
set2=set([b1,b2,b3])

#1
x=set1-set2
print(x)
#2
ans1=set1<=set2
ans2=set1>=set2
print(ans1)
print(ans2)
#3
set3=set1&set2

print(set3)

 #dictionary
 #ques1
name=input("enter the name")
marks=input("enter the marks")
d={'name':name,'marks':marks}
print(d)

#ques2
l="mississippi"
m=l.count('m')
i=l.count('i')
s=l.count('s')
p=l.count('p')

d={'m':m,
  'i':i,
  's':s,
  'p':p}

print(d)



