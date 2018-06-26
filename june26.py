#assignment26june
import sqlite3
#question1
open=sqlite3.connect('test1.db')
print("opened databse successfully")

#open.execute( '''Create table BOOKS(BookId INT PRIMARY KEY NOT NULL,TitleId INT,Location varchar(30),Genre VARCHAR(10));''')

#open.execute('''Create table Title(TitleId int primary key,Title varchar(35),ISBN int,Publisher_ID int,Publication_Year int);''')

#open.execute('''Create table PUBLISHER(Publisher_ID int primary key,Name varchar(15),Street_Address varchar(50),
    #Suite_Number int,Zip_Code_ID int);''')

#open.execute('''Create table Zip_Code(Zip_Code_ID int primary key,City varchar(15),State varchar(20),Zip_Code int);''')
#open.execute('''Create table Author(AuthorID int primary key,FirstName varchar(15),MiddleName varchar(15),LastName varchar(15));''')
#open.execute( '''Create table Author_Titles(Author_Title_ID int primary key,AuthorID int ,TitleId int );''')

#print('Table Created')

#question2
#open.execute("Insert into BOOKS(BookId,TitleId,Location,Genre) VALUES (101, 02,'rack1', 'TOC')")
#open.execute("Insert into BOOKS(BookId,TitleId,Location,Genre) VALUES (111, 06,'rack2','dbms')")
#open.commit()
#print("inserted")

xyz=open.execute("Select BookId,TitleId,Location,Genre from BOOKS")
for row in xyz:
    print("BookId =", row[0])
    print("TitleId =", row[1])
    print("Location =", row[2])
    print("Genre =", row[3], "\n")
print("records created")

#open.execute("INSERT into Title(TitleId,Title,ISBN,Publisher_ID,Publication_Year) VALUES ( 2, 'xyz',09876,899,1978)")
#open.commit()
#print("insert")
w=open.execute("SELECT TitleId,Title,ISBN,Publisher_ID,Publication_Year from Title")
for row in w:
    print("TitleId =", row[0])
    print("Title =", row[1])
    print("ISBN =", row[2])
    print("Publisher_ID =", row[3])
    print("Publication_Year =", row[4], "\n")
print("records created")

#open.execute("INSERT INTO PUBLISHER(Publisher_Id,Name,Street_Address,Suite_Number,Zip_Code_ID) VALUES ( 899, 'gopal',11,909,876)")
#open.commit()
#print("insertrd!!")
x=open.execute("SELECT Publisher_Id,Name,Street_Address,Suite_Number,Zip_Code_ID from PUBLISHER")
for row in x:
    print("Publisher_ID =", row[0])
    print("Name =", row[1])
    print("Street_Address =", row[2])
    print("Suite_Number =", row[3])
    print("Zip_Code_ID =", row[4], "\n")
print("records created")

#open.execute("INSERT INTO Zip_Code(Zip_Code_ID,City,State,Zip_Code) VALUES ( 876, 'jalandhar','punjab',077)")
#open.commit()
#print("done")
y=open.execute("SELECT Zip_Code_ID,City,State,Zip_Code from Zip_Code")
for row in y:
    print("Zip_Code_ID =", row[0])
    print("City =", row[1])
    print("State =", row[2])
    print("Zip_Code =", row[3], "\n")
print("records created")

#open.execute("INSERT INTO Author(AuthorID,FirstName,MiddleName,LastName) VALUES ( 23, 'isha','m','prasher')")
#open.commit()
#print("jai mata di")
z=open.execute("SELECT AuthorID,FirstName,MiddleName,LastName from Author")
for row in z:
    print("AuthorID =", row[0])
    print("FirstName =", row[1])
    print("MiddleName =", row[2])
    print("LastName =", row[3], "\n")
print("records created")

open.execute("INSERT INTO Author_Titles(Author_Title_ID ,AuthorID  ,TitleId) VALUES ( 0, 23,2)")
open.commit()
print("dffa ho")
a=open.execute("SELECT Author_Title_ID ,AuthorID  ,TitleId from Author_Titles")
for row in a:
    print("Author_Title_ID =", row[0])
    print("AuthorID =", row[1])
    print("TitleId =", row[2], "\n")
print("records created")

#ques3
open.execute("UPDATE BOOKS set Genre = 'mechanical' where BookId=111 and TitleId=06")
open.commit()
xyz=open.execute("SELECT BookId,TitleId,Location,Genre from BOOKS")
for row in xyz:
    print("BookId =", row[0])
    print("TitleId =", row[1])
    print("Location =", row[2])
    print("Genre =", row[3], "\n")


print("records updated")
















































































































































































































































































































