# input() - A function that prompts the user to enter the data
#           returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you?: "))     # int(input()) - typecasting method

print(f"My name is {name}")
print(f"I am {age} years old")

# Exercise: Rectangle Area Calculation
# Area = length * width

length = float(input("Enter length: "))        # Enter length: 16.5
width = float(input("Enter width: "))          # Enter width: 4.52
area = length * width                          # The area is 74.58cm²

print(f"The area is {area}cm²")   # numlock + alt + 0178 = " ² "