from datetime import date, datetime

class college:
   def  __init__(self,Name,profession) :
      self.name=Name
      self.prof=profession
      self.date=date
     
   def show(self):
       print(date.today())
       print("Welcome to! ",self.name,"\nHope you're doing very well and we are sure that you will be happy joining this college as a ",self.prof)

class employee:
   def __init__(self,Name,profession) :
      super().__init__()

college1= college("Govt. Post Graduate Collge Mardan","Lecturer")
college2= college("Govt. Post Graduate Collge Mardan","Audit Officer")
college3= college("Govt. Post Graduate Collge Mardan","Gardner")
college1.show()
college2.show()
college3.show()