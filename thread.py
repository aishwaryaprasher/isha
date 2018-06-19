
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