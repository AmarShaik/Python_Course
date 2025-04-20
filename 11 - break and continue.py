# break – Exit the Loop Early
# It stops the loop completely, even if the condition is still True.
# You use break when you want to exit the loop based on a certain condition.

# continue – Skip the Current Iteration
# It skips the rest of the loop body for the current iteration and jumps back to the condition check.
# You use continue when you want to skip over just one loop cycle and keep going.


# for i in range(12):
#   if(i == 10):
#     print("Skip the iteration")
#     continue
#   print("5 X", i, "=", 5 * i)

i = 0
while True:
    print(i)
    i = i + 1
    if (i % 100 == 0):
        break