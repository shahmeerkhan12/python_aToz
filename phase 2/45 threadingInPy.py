# thread is flow of execution. Like a seperate order of instructions
# however each thread takes a turn to run to achieve concurrency
# GIL (global interpreter lock) allows only one thread to take hold of the interpreter at one time
# tasks can be
# cpu bound := spends most of its time waiting for internal events, these task use the Multiprocessing technique
# i/o bound := spends most of // // //   //     // external // , like user inputs and web scraping etc, they use multithreading tech

import threading
import time

def walk():
   time.sleep(2)
   print("you are walking")
def talk():
   time.sleep(3)
   print("you are talking")
def run():
   time.sleep(4)
   print("you are running")

x=threading.Thread(target=walk,args=())
x.start()
y=threading.Thread(target=talk,args=())
y.start()
z=threading.Thread(target=run,args=())
z.start()
#if you want to sync the threads to the main thread use the follwing statement
# x.join()
# y.join()
# z.join()

# count the number of currently running active threads
print(threading.active_count())

#  Return a list of all Thread objects currently alive.

#  The list includes daemonic threads, dummy thread objects created by current_thread(), and the main thread.#
#  It excludes terminated threads and threads that have not yet been started.
print(threading.enumerate())
print(time.perf_counter())