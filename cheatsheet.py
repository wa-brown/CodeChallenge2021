# this file contains some common code snipets to help us develop faster.

# ----------------------------------------------------------------------------------------
# files
reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
finally:
    reader.close()

# 'r' 	Open for reading (default)
# 'w' 	Open for writing, truncating (overwriting) the file first
# 'rb' or 'wb' 	Open in binary mode (read/write using byte data)
with open('dog_breeds.txt', 'r') as reader:
    # Further file processing goes here

# more info on reading a writing files: https://realpython.com/read-write-files-python/
# ----------------------------------------------------------------------------------------


# OOP in python

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


# call object class
>>> miles = Dog("Miles", 4)

>>> miles.description()
'Miles is 4 years old'

>>> miles.speak("Woof Woof")
'Miles says Woof Woof'

>>> miles.speak("Bow Wow")
'Miles says Bow Wow'
