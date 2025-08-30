# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Durgesh naie. 20 rs daadhi khakhori free")
# engine.runAndWait()


import os

path = '/PYTHON JOURNEY'  # or leave blank for current directory
contents = os.listdir(path)
for entry in contents:
    print(entry)

