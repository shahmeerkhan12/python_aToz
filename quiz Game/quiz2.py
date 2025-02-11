
from hmac import new


def newGame():
   questions_num=1
   guessess = []
   correct_guses=0
   #outer looop to display the questions from the dict
   for key in questions:
      print(key)
      # inner looop to display the relevant options
      for i in options[questions_num-1]:
         print(i)
      
      guess=input("your answer:  ")
      guess=guess.lower()
      guessess.append(guess)
      correct_guses += checkAns(questions[key],guess)
      questions_num += 1
   #lets get the score
   score(correct_guses,len(questions))
   playAgain()
      # >>>>>>>>>>>
def checkAns(answer,guess):
   if answer==guess:
      print('correct')
      #remember to return number
      return 1
   else:
      print('wrong')
      return 0
# score method
def score(c_g,total):
   print("your score is >>> ")
   score = int(c_g/total*100)
   print("   >>>>  ",score)
questions={
   "who is he?":"ali",
   "how are you?":"fine",
}
options = [
   [
      "a. ali","b. ahmad"
   ],
   [
      "a. nice","b. fine"
   ],
]
def  playAgain():
   p_again=input (("play again! (y/n): "))
   p_again = p_again.lower()
   if p_again == "y":
      newGame()
   else:
      print ("bye bye")

   
newGame()
