# =============== TEST 1: Using range to print a simple list.

# Print a list of 10 elements from 0-9
# newList = list(range(10))
# print(newList)

# Print a list of even / odd integers.
# evenNum = list(range(0, 10, 2))
# oddNUm = list(range(1, 10, 2))
# print("Even: {}".format(evenNum))
# print("Odd: {}".format(oddNUm))




# =============== TEST 2: Accessing string elements via index.

# newString = "asddgffgsrdgsfbdvgr"
# print(newString.index('d'))    # returns index
# print(newString[2])            # returns character




# =============== TEST 3: Playing more with ranges and for loops

# example 1

# smallDec = range(0, 10)
# print(smallDec)
#
# print(smallDec.index(3))
#
# oddNum = range(1, 10000, 2)
# print(oddNum)
#
# print(oddNum[954])


# example 2

# sevens = range(7, 1000000, 7)
# x = int(input("Enter positive int < a mill: "))
#
# if x in sevens:
#     print("{} is divisible by 7".format(x))
# else:
#     print("{} is NOT divisible by 7".format(x))


# example 3

# customRange = smallDec[::2]
# print(customRange)
# print(customRange.index(4))


# example 4

# decimals = range(0, 100)
# print(decimals)
#
# myDecimals = decimals[3:40:3]
# print(myDecimals)
#
# print()
#
# for i in myDecimals:
#     print(i, end=' ')
#
# print()
# print()
# print("="*50)
# print()
#
# # Same as above for loop
# for i in range(3, 40, 3):
#     print(i, end=' ')




# =============== TEST 4: More with ranges


# example 1 - iterating backwards

# r1= range(0, 100)
# # r1= "HELLO WORLD"
# print(r1)
#
# for i in r1[::-2]:
#     print(i)
#
# print()
#
# for i in range(99, 0, -2):
#     print(i)
#
# print()
#
# print(range(0, 100)[::-2] == range(99, 0, -2))




# =============== TEST 5: Further experimentation with ranges

# Predict what will happen in the below program without running it.

o = range(0, 100, 4)     # Take a variable o and assign it the range starting at 0, going to 99, and incrementing by 4.
print(o)                 # Prints: range(0, 100, 4)

p = o[::5]               # Take a variable p and assign it the range starting at 0, going to 99,
                         # and incrementing by 4x5 or 20.

print(p)                 # Prints: range(0, 100, 20)
for i in p:              # Starting from 0 and ending at 80, prints all numbers incrementing by 20.
    print(i)             # We will get 0, 20, 40, 60, 80

# Use for loop to print o.
print()
for i in o:
    print(i)