# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Durgesh naie. 20 rs daadhi khakhori free")
# engine.runAndWait()


# import os

# path = '/PYTHON JOURNEY'  # or leave blank for current directory
# contents = os.listdir(path)
# for entry in contents:
#     print(entry)



# ================practice set 2==================
# QUESTION 1

# name = input("Enter your name: ")
# print("Good afternoon", name)


# # QUESTION 2

# letter = '''Dear <|name|>
#     you are selected 
#     <|Date|>'''
# print(letter.replace("<|name|>","krishna").replace("<|Date|>","29Aug2025"))

# QUESTION 3

# name = "krishna is   a  good boy"
# print(name.find("  "))

#===================CHAPTER 4 PRACTICE SET======================

# fruits = []
# fruit1 = input("Enter the Fruit name: ")
# fruits.append(fruit1)
# fruit2 = input("Enter the Fruit name: ")
# fruits.append(fruit2)
# fruit3 = input("Enter the Fruit name: ")
# fruits.append(fruit3)
# fruit4 = input("Enter the Fruit name: ")
# fruits.append(fruit4)
# fruit5 = input("Enter the Fruit name: ")
# fruits.append(fruit5)
# fruit6 = input("Enter the Fruit name: ")
# fruits.append(fruit6)
# print(fruits)



# =====================CHAPTER 5 PRACTICE SET===========================
# words = {
#     "madat": "help",
#     "kursi": "chair",
#     "billi": "cat"
# }
# word =input("enter the word you want meaning of: ")
# print(words[word])



# s = set()
# number1 = int(input("enter the number1: "))
# s.add(number1)
# number2 = int(input("enter the number2: "))
# s.add(number2)
# print(s)



d = {}
name = input("enter your name: ")
language = input("enter language name: ")
d.update({name: language})

name = input("enter your name: ")
language = input("enter language name: ")
d.update({name: language})

name = input("enter your name: ")
language = input("enter language name: ")
d.update({name: language})

name = input("enter your name: ")
language = input("enter language name: ")
d.update({name: language})

name = input("enter your name: ")
language = input("enter language name: ")
d.update({name: language})

name = input("enter your name: ")
language = input("enter language name: ")
d.update({name: language})

print(d)                 #the values entered later will be updated


