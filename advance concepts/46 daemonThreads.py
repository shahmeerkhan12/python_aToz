# daemon threads:= are those threads that executes regardless of the main program flow or main thread
# non-daemon threads:= will execute till their task is completed and they cannot be killed.
# the main program will not wait for daemon threads to complete before exiting
# use cases
#  "useful for backgound tasks, waiting user inputs, and other long running processes"

import threading
import time

def timer():
   count = 0
   while True:
      time.sleep(1)
      count += 1
      print()
      print("your here for ",count, " seconds")
print()
# example of non - daemon threads
# x = threading.Thread(target=timer,args=(),) 
# to turn a thread into daemon threads
x = threading.Thread(target=timer,args=(),daemon=True)
x.start()
# main thread
answer = input("what is your answer? ")
# u can also check out if a thread is daemon or not
print(x.isDaemon())

# another method for daemon threads is like
x.setDaemon(True) # but remember you cannot do it if the thread is running, so put it immediatley before the start() method 
