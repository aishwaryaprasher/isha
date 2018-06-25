import re
str=" Abc is 18 years old"\
    "Xyz is 19 years old"\
    "Mno is 20 years old"
name=re.findall("[A-Z][a-z]*",str)
print(name)
age=re.findall("\d{1,3}",str) #prints decimals  from minimum range 1 to max 3
print(age)
age=re.findall("\D",str) #print everything except decimals
print(age)
a="sat,cat,mat,kat,at"
x=re.compile("[r]at")
st=x.sub("abc",a)
print(a)
email="abc@gmail.com jaimaaambey sarararara??"
match=re.findall("[\w]{1,20}[@][\w]{1,10}[.][a-zA-Z]{2,5}",email)
print(match)
phone="+91-9876-543210"
matchp=re.findall("[+][\d]{2}[-][\d]{4}[-][\d]{6}",phone)
print(matchp)