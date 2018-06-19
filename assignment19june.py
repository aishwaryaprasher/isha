#assignment 19june
# #Ques1
import threading
import time
import math

class Abc(threading.Thread):
    def __init__ (self):
        threading.Thread.__init__(self)
    def run(self):
        time.sleep(5)
        print("thread sleeps for 5 seconds")
a=Abc()
a.start()
a.join()
#ques2
import threading
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(1)
        print("value of", self.h)

for i in range(10):
    thread1=    Mythread(i)
    thread1.start()
    thread1.join()
print("active threads are", threading.activeCount())

#Ques3
import threading
import time
class Mythread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        n=2
        l=(1,2,3,4,5)
        for i in l:
            time.sleep(n)
            print("element is %d"%i)
            n=n+2


thread = Mythread("")
thread.start()
#ques4
import threading
import time
import math
class Factorial(threading.Thread):
    def __init__ (self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(2)
        print("FACTORIAL OF GIVEN NO--> %d"%math.factorial(self.h))
fact=1
time.sleep(2)
i=int(input("ENTER ANY NUMBER"))
thread1=Factorial(i)
thread1.start()
thread1.join()

