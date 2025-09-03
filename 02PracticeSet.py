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



# d = {}
# name = input("enter your name: ")
# language = input("enter language name: ")
# d.update({name: language})

# name = input("enter your name: ")
# language = input("enter language name: ")
# d.update({name: language})

# name = input("enter your name: ")
# language = input("enter language name: ")
# d.update({name: language})

# name = input("enter your name: ")
# language = input("enter language name: ")
# d.update({name: language})

# name = input("enter your name: ")
# language = input("enter language name: ")
# d.update({name: language})

# name = input("enter your name: ")
# language = input("enter language name: ")
# d.update({name: language})

# print(d)                 #the values entered later will be updated


# ======================CHAPTER 6 PRACTICE SET============================

# a = int(input("enter the num A: "))
# b = int(input("enter the num B: "))
# c = int(input("enter the num C: "))
# d = int(input("enter the num D: "))
# if(a>b):
#     print("A is greater")

# elif(b>c):
#     print("B is greater")

# elif(c>d):
#     print("C is greater")

# elif(d>a):
#     print("D is greater")



# ===================QUESTION NO: 3===========================
# m1 = "Make a lot of money"
# m2 = "buy now"
# m3 = "subscribe this"
# m4 = "click this"

# message = input("Enter you comment: ")
# if(m1 in message or m2 in message or m3 in message or m4 in message):
#     print("this comment is spam")
# else:
#     print("this comment is not a spam")




username = input("Enter your username: ")
if(len(username)>10):
    print("contains more than 10 characters")
else:
    print("contains less than 10 characters")


l = ["harry", "krishna", "pinki", "ritu"]
if(username in l):
    print("your name is in the list")
else:
    print("your name is not present in the list")