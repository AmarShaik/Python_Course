#In Python, a string is a sequence of characters enclosed in single ('), double ("), or triple quotes (''' or """ """).
# Strings are immutable and are ordered, meaning they cannot be changed after creation.

name = "Steve"
friend = "Robert"
anotherFriend = 'Chris'
apple = '''He said, 
Hi Steve
hey I am good
"I want to eat an apple'''

print("Hello, " + name)
# print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop\n")
for character in apple:
    print(character)