tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)


# Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[0])   # apple
print(fruits[-1])  # cherry


# Length of a Tuple
fruits = ("apple", "banana", "cherry")
print(len(fruits))  # 3


# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, 4, 5)
