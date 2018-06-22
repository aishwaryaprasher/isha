#f=open("text1.txt","r")
#print (f.readline()) #prints first line
#print (f.readline()) #prints first as well as second line
#print (f.readlines()) #prints all lines in a list
#print(f.close()) #used so that memory is not used again n again in buffer

#f=open("text1.txt","w")
#f.write("teri maa ki ankh") #adds this write text in that text file (over written)

#print(f.read())


#f=open("text1.txt","w")
#a=["a\n b\n"]
#f.readlines(a)

#use of with
with open("text1.txt","w") as f:
    a=["a\n","b\n"]
    f.writelines(a)
    print(f.tell())
with open("text1.txt","w") as f:
  f.seek(5,0)
  print(f.tell())