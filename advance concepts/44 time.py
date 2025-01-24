# lets check out the various time methods python provides
#time.ctime(0) := provides the time expressed in seconds since epoch, into a readable format
#time.localtime()
#time.gmtime()
#epoch := computer thinks when time begin from this point
import time
# M-1
print(time.ctime(time.time()))
# M-2 format the time object
timeObject = time.localtime()
print(timeObject)# would return a time object tuple consisting of year,month,day,h,m,s,weekday,yearday
# lets give a readable format to the timeObject 
local_time=time.strftime("%B %A %Y %H:%M:%S",timeObject)
print(local_time)
# M-3
utctime= time.gmtime()
print(utctime)
