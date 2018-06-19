0#import threading
import time
#class Mythread(threading.Thread):
 #   def __init__(self,i):
  #      threading.Thread.__init__(self)
   #     self.h=i
    #def run(self):
     #   time.sleep(5)
      #  print("value of",self.h)
#thread1 = Mythread(2)
##thread1.start()
#thread2 = Mythread(2)
#thread2.start()
####

import threading
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(3)


        print("value of", self.h)


for i in range(10):
    thread1=    Mythread(i)
    thread1.start()

print("active threads are",threading.activeCount())
