class school:
   def has_teachers(self):
      print("All schools has teachers.")
      
class College:
   def has_professors(self):
      print("All schools has Professors.")

class student(school,College):# inherited from more than 2 classes
   def has_student(self):
      print("Both schools and colleges have students.")
   

Student= student()
print("-----------------------------------")
Student.has_professors()
Student.has_teachers()
Student.has_student()
print("-----------------------------------")

