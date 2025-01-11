# # print("Chal Bhai")
# import pyjokes
# print("Printing Jokes")
# joke = pyjokes.get_joke()
# print(joke)
# """
# so  Thanks budyy
# """

# # Pratice SEt
# print('''Muliline STings
#       Twinkle Twinkle''')
"""
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate',125)
engine.say("Killer Boss")
engine.runAndWait()
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.say("Hello World! I Hate Programming")

engine.runAndWait()
engine.stop()"""
"""VOLUME"""
# volume = engine.getProperty('volume')   
# print (volume)                         
# engine.setProperty('volume',1)

import os

directory_path = 'Chapter_1'

contents = os.listdir(directory_path)

for item in contents:
     print(item)