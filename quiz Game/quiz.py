# a simple python quiz game



print("_____________________________")
def new_game():
   guesses = [] #stores the user guesses
   correct_guesses= 0
   question_num=1

   for key in questions :
      print("------------------------------")
      print(key)
      for i in options[question_num-1]:
         print(i)

      #outer for loop, take user input option for each question
      guess= input("Choose the correct options,(A,B,C,or,D)")
      guess = guess.upper()

      # to store all of user input options, we have
      guesses.append(guess)

      # to check whether the user options are correct or not
      correct_guesses += check_answer(questions[key],guess) 
      question_num +=1 
      # print(questions[key])

   #display the result
   display_score(correct_guesses,guesses)

   print("_____________________________")
def check_answer(answer,guess):
   
   if answer==guess:
      print("Correct!")
      return 1
   else :
      print("Wrong")
      return 0
   print("_____________________________")
def display_score(correct_guesses,guesses):

   print("----------------------")
   print("RESULTS:")#heading
   print("----------------------")
   
   #lets display the correct ansers from the questions dictionary using for loop
   print("Answers: ",end =" ")
   for i in questions :
      print(questions.get(i), end = " ")
   print()
    
    # now lets print out the user guesses
   
   print("Guesses: ",end =" ")   
   for i in guesses :
      print(i, end = " ")
   print()

 # lets print the score
   score = int((correct_guesses/len(questions))*100)
   print()
   print("your score is: "+ str(score) + "%")
   print("_____________________________")
def play_again():

   play_again = input("Do you want to play again? (yes/no): ")
   play_again=play_again.upper()

   if play_again == "YES":
      return True
   else :
      return False
   print("_____________________________")

#dictoinary
questions ={
   "who created python? ":"A",
   "who was the father of computer?":"B",
   "when did python introduced?":"C",
   "python is an interpreted language?":"D"
         }
#2d list
options=[["A. Guido Von Rosum","B. Kalan Matt","C. Bred Nathan"],
         ["A. Ali Baba","B. Charles Babbage","C. None"],
         ["A. 1989","B. 1891","C. 1991","D. 2000",],
         ["A. No","B. Don't know","C. May Be","D. Yes",]
]

new_game()

# we use a while loop whether to play again or exit

while play_again() :
   new_game()

print("Come again, next time!")