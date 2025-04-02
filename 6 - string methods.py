# Strings are immutable
a = "!!!Steve!! !!!!!!!!! Steve"
print(len(a))  # 26
print(a)  # !!!Steve!! !!!!!!!!! Steve
print(a.upper())  # !!!STEVE!! !!!!!!!!!! STEVE
print(a.lower())  # !!!steve!! !!!!!!!!!! steve
print(a.rstrip("!"))  # !!!Steve!! !!!!!!!!!! Steve
print(a.split(" "))  # ['!!!Steve!!', '!!!!!!!!!', 'Steve']

blogHeading = "introduction tO jS"
print(blogHeading.capitalize())  # Introduction to js

str1 = "Welcome to the Console!!!"
print(len(str1))  # 25
print(len(str1.center(50)))  # 50
print(a.count("Robert"))  # 0

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))  # True
print(str1.endswith("to", 4, 10))  # True

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))  # -1
# print(str1.index("ishh"))  # Would raise an error

str1 = "WelcomeToTheConsole"
print(str1.isalnum())  # True
str1 = "Welcome"
print(str1.isalpha())  # True

str1 = "hello world"
print(str1.islower())  # True

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())  # False

str1 = "         "  # Using Spacebar
print(str1.isspace())  # True
str2 = "  "  # Using Tab
print(str2.isspace())  # True

str1 = "World Health Organization"
print(str1.istitle())  # True

str2 = "To kill a Mocking bird"
print(str2.istitle())  # False

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))  # True

print(str1.swapcase())  # pYTHON IS A iNTERPRETED lANGUAGE

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())  # His Name Is Dan. Dan Is An Honest Man.


# Explanation of String Methods:
#
# 1. Case Modification
# upper(): Converts all characters to uppercase.
# lower(): Converts all characters to lowercase.
# capitalize(): Converts the first letter to uppercase and makes the rest lowercase.
# swapcase(): Swaps uppercase to lowercase and vice versa.
# title(): Capitalizes the first letter of each word.
#
# 2. String Manipulation
# replace(old, new): Replaces all occurrences of old with new.
# split(separator): Splits a string into a list based on separator.
# rstrip(chars): Removes trailing characters (default whitespace or specified ones).
#
# 3. String Analysis
# len(string): Returns the length of the string.
# count(substring): Returns the number of occurrences of substring.
# find(substring): Returns the index of substring (or -1 if not found).
# index(substring): Similar to find(), but raises an error if substring is not found.
# startswith(substring): Checks if the string starts with substring.
# endswith(substring): Checks if the string ends with substring.
#
# 4. String Checks
# isalnum(): Returns True if all characters are alphanumeric.
# isalpha(): Returns True if all characters are alphabetic.
# islower(): Returns True if all characters are lowercase.
# isprintable(): Returns False if the string contains unprintable characters (like \n).
# isspace(): Returns True if the string contains only whitespace.
# istitle(): Returns True if the string follows title case.