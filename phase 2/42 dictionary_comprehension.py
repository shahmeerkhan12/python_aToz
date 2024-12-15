# Dict Comprehension := can create new dictionaries using an expression that replaces lambda fun and forloops as well
# syntax1 :=    { key exp for (key,value) in iterable}
# syntax2 :=    { key exp for (key,value) in iterable conditions(if any)}
# syntax3:=    { key (if/else) for (key,value) in iterable conditions(if any)}

# Example 01 := 
#---------------------------------------------------------------------------------------------------------------------------------
# similarly we can do the following
TinF = {"Germany":40,"Turkey":65,"England":48,"Japan":99,"Malaysia":78,"Pakistan":49,"India":40,"Afghanistan":40,"Bangladesh":45}
TinC = {key:(round((value-32)*(5/9))) for (key,value) in TinF.items()}
# print(TinC)

# #Example 02
# #---------------------------------------------------------------------------------------------------------------------------------
# env_health = {"Germany":40,"Turkey":45,"England":50,"Japan":59,"Malaysia":48,"South Korea":42,"Pakistan":49,"India":40,"Afghanistan":40,"Bangladesh":45}
# # lets turn take the Good Health (>=45)
# good_health = {key:value for (key,value) in env_health.items() if(value>=45)}
# print(good_health)

# exampe 03
#---------------------------------------------------------------------------------------------------------------------------------
Temp_F = {"Germany":40,"Turkey":65,"England":48,"Japan":99,"Malaysia":78}
WarmAndCold = {key:("warm" if value>60 else "cold") for (key,value) in Temp_F.items()}
# print(WarmAndCold)
# exampe 04
# if the conditions are more challenging and takes alot of space then
# syntax 3:=    { key: function(value) for (key,value) in iterable}
# define a function and pass the value as parameter to perform the required functions
#---------------------------------------------------------------------------------------------------------------------------------
def climate(val):
   if val>=40:
      return "very Hot"
   elif val>=35:
      return "hot"
   elif val>=25:
      return "moderate"
   else :
      return "cold"
   
tempRecord = {key:climate(value) for (key,value) in TinC.items()}
print()
print(tempRecord)