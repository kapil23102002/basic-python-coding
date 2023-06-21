greeting = "hello, "
name = "kapil"
# print(greeting + name) #add two strings
m= greeting + name # Concatenating two strings
print(m)

print(name[2])
print(name[0:2])
print(name[0:]) # len(0) to end
print(name[:3]) # len(0) to len(3)
print(name[0:4:2]) # print every 2 letter

# String Function

story = "there is a boy who has a sports car  but stil he is in second last position in olympic race"

print(len(story))  # find length of string
print(story.endswith("hello")) # last word (True & False)
print(story.count("a")) # count total "a" in story
print(story.capitalize()) # first letter capital
print(story.find("boy")) # place of boy 
print(story.replace("boy", "kapil"))

''' ESCAPE SEQUENCE CHARACTER
\n -----new line
\t -----tab
\' -----single quote
\\----- back slash 
'''

# question(1) 

name= input("Enter your name : ")
print("Good Afternoon, "+ name)

# question(2) Template with name and Date

letter = '''Dear, <|NAME|> ,
You are Selected !

Date : <|DATE|> '''
name = input("Enter your Name\n ")
date = input("Enter date\n")
letter = letter.replace("<|NAME|>" , name)
letter = letter.replace("<|DATE|>" , date)
print(letter)

# question(3) detect double space in string

st = " My name is kapil and i live  in Indore"
doubleSpace = st.find("  ")
print(doubleSpace)

# question(4) format a letter using escape sequence

leter = "Dear kapil,\n You are Selected ! \n Date \t1.1.2000 "
print(leter)
