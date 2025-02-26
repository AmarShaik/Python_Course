# typecasting - The process of converting a variable from one dat atype to another
#               str(), int(), float(), bool()

name = "Stephen"
age = 25
gpa = 8.8
is_student = True

gpa = int(gpa)
print(gpa)              # 8

age = str(age)
age += "1"              #251
# age = float(age)
print(age)              # 25.0

# age = str(age)
# print(age)
# print(type(age))       #<class 'str'>

name = bool(name)
print(name)             #True

