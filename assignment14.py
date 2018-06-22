#assignment14
# #Question1
f= open("text2.txt",encoding="utf8")
print(f.read())
f.close()

#question2
with open("text2.txt", encoding="utf8") as f:
    f.seek(0,0)
    a=f.read()
    b=a.split(" " or "." or "," or ".\n" or "'s ")
i=0
count=0
for i in range(0,len(b)):
    print("Total "+b[i]+"'s in File-%d"%int(b.count(b[i])))


#question3
with open("text2.txt",encoding="utf8") as f:
    with open("abc.txt", "w") as f1:
        for line in f:
            f1.write(line)
#Question4
with open("xyz.txt",encoding="ISO-8859-1") as f1, open("xyz1.txt",encoding="ISO-8859-1") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1 + line2)

#question5
rlist=[]
import random
for i in range(0,10):
    rlist.append(random.randrange(0,100))
    rlist[i]=str(rlist[i])
print(rlist)
print(sorted(rlist))
f1=open("random.txt","r+")
f1.writelines(rlist)
print(f1.readline())
f1=open("random1.txt","r+")
f1.writelines(sorted(rlist))
print(f1.readline())
f1.close()

