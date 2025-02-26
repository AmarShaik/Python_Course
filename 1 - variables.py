#Variablle = A container for a value (string, integer, flot, boolean)
#            A variable behaves as if it was the value it contains

#Strings
first_name = "Stephen"
food = "pasta"
email = "stephen123@fake.com"

#fstrings - provide a concise and readable way to format strings

print(f"My first name is {first_name}")   # My first name is Stephen
print(f"My email is {email}")             # My email is victor123@fake.com
print(f"My favourite food is {food}")     # My favourite food is pasta

#Integers
age = 25
quantity = 3
num_of_students = 50

#Float
price = 10.99
gpa = 8.8
distance = 5.5

print(f"Distance is {distance}km")     # Distance is 5.5km
print(f"Food price is ${price}")       # Food price is $10.99

# Boolean
for_sale = True

if for_sale:
    print("The item is for sale")     # The item is for sale - since, the boolean we have given is True if not, False
else:
    print("The item is not for sale")