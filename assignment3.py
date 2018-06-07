#assignment3

#ques1

print("ENTER THE LIST")
a=input()
l=[]
l.append(a)
print(l)

#ques2

l.append("google")
l.append("apple")
l.append("facebook")
l.append("microsoft")
l.append("tesla")
print(l)

#ques3

x=l.count("google")
print("no of times google occurs-->")
print(x)

#ques4

l2=[5,7,0,9,12,6,1]
l2.sort()
print(l2)

#ques5
l3=[15,37,5,93,122,622,11]
l3.sort()
print(l3)
l4=l2+l3
l4.sort()
print(l4)

#ques6
y=l2.pop()
print(y)

#extraques
for(i=0;i<l4.len;i++)
    if(l4[i]%2==0)
x=0;
x++