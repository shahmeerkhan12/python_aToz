# let we want to make a file and then write to it some text

text="Oh! it seems too easy to write to a file in Python as compare to C++."
text2="\n\nProfessor told me that after learning c++, You will enjoy learning Python."
with open('MyTextFile.txt','a') as file:
   file.write(text)
   file.write(text2)

# the next time you write to a file, you can overwrite the existing text or you can append to the existing
# let i append to the exsiting text then i shoudl use the letter 'a' instead of w or r.
   
newtext="\nI remember oneday Professor told me that after learning c++, You will enjoy learning Python."
text2="\nProfessor told me that after learning c++, You will enjoy learning Python."
line_5= "\nline 5 added"
# i can declare and initialize this text above opening file statement and then add this text but
# i will do it here. these statements will append the new text to the existing text
with open('MyTextFile.txt','a') as file: # 'a' for append
   file.write(line_5)

