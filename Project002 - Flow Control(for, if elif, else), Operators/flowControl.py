# =================== TEST 1

# for i in range(1, 12):
#     print("No {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 4))


# =================== TEST 2

# myName = input("What is your name?: ")
# age = int(input("What is your age, {}?: ".format(myName)))
# print("Your name is {} and you are {} years old.".format(myName, age))
#
# if 100 >= age >= 21:
#     print("You can drink.")
# elif age < 21:
#     diff = 21 - age
#     print("You can drink in about {} years.".format(diff))
# elif age > 100:
#     print("You should be dead!")


# =================== TEST 3

# guess = int(input("Guess a number between 1 and 10: "))
# if guess != 5:
#     if guess < 5:
#         print("Guess higher: ")
#     else:
#         print("Guess lower: ")
#     guess = int(input())
#     if guess == 5:
#         print("Well done! You got it!")
#     else:
#         print("Incorrect")
# else:
#     print("Correct the first time!")


# =================== TEST 4

# age = int(input("What is your age?: "))
# # if (age >= 16) and (age <= 65):
# if 16 <= age <= 65:
#     print("Hello!")


# =================== TEST 5

# bird = "Moluccan Cockatoo"
# letter = input("Enter a word: ")
# if letter in bird:
#     print("'{}' IS in '{}'".format(letter, bird))
# else:
#     print("'{}' is NOT in '{}.'".format(letter, bird))


# =================== TEST 6

# name = input("Give me your name: ")
# age = int(input("Give me your age as an integer, {}: ".format(name)))
#
# if (age >= 18) and (age < 31):
#     print("Welcome to the holiday, {}.".format(name))
# elif age > 30:
#     print("Sorry, {}, but you are too old for this.".format(name))
# else:
#     print("Sorry, {}, but you are too young for this.".format(name))


# =================== TEST 7 - looping

# for i in range (1, 10):
#     print("i is currently {}".format(i))


# =================== TEST 8 - building an int from a string

# stringNumber = "8,564,765,567,567,234,456,345"
# cleanedStringNumber = ''
# for i in range (0, len(stringNumber)):
#     if stringNumber[i] in "0123456789":
#         cleanedStringNumber = cleanedStringNumber + stringNumber[i]
#         # print(stringNumber[i], end='') # instead of end being a new line, it should be inline
#
# newNum = int(cleanedStringNumber)
# print("Number is {}".format(newNum))


# =================== TEST 9 - building an int from a string (improved code)

# stringNumber = "8,564,765,567,567,234,456,345"
# cleanedStringNumber = ''
#
# for char in stringNumber:
#     if char in '0123456789':
#         cleanedStringNumber = cleanedStringNumber + char
# newNum = int(cleanedStringNumber)
# print("Number is {}".format(newNum))


# =================== TEST 10 - reading stuff from a list

# for state in ["not ere", "eradc dsf", "sdfsd", "asdfsd sd sdf"]:
#     print("This person is {}".format(state, end=''))


# =================== TEST 11 - incrementing by a number in a loop

# for i in range (0, 100, 5): # go from 0 to 99, but in increments of 5
#     if i % 2 == 0:
#         print(i)


# =================== TEST 12 - More string formatting

# for i in range (1,10):
#     for j in range (1, 10):
#         print("{} x {} = {}".format(i, j, i*j))
#     print()


# =================== TEST 13 - Breaking out of loops, continue

# todo_list = ["hw", "studying", "reading", "job", "wasting time", "exercising"]
# for todo in todo_list:
#     if todo == "wasting time":
#         print("IGNORE TASK: {}".format(todo))
#         continue # continue stops processing and moves to next value; break will completely stop everything
#     print("Task: {} ".format(todo))


# =================== TEST 14 - breaking out of loops

# pets = ["dog", "cat", "fish", "hamster", "cockatoo", "snake"]
#
# loudPet = ''
# for pet in pets:
#     if pet == "cockatoo":
#         loudPet = pet
#         break
# else:
#     print("These animals are cool")
#
# if loudPet == "cockatoo":
#     print("Cockatoos are way too loud!")


# =================== TEST 15 - Augmented assignment (+=)

# num = "334,324,678,784,582,575,385"
# cleanNum = ''
#
# for i in range(0, len(num)):
#     if num[i] in "0123456789":
#         cleanNum += num[i]
#
# intClean = int(cleanNum)
# print(intClean)


# =================== TEST 16 - CHALLENGE - Make a program that takes an ip address and spits out how many segments it
#                                           has along with the length of each segment.

# SOLUTION

ipAddress = input("Enter an IP address: ")
# ipAddress = "127.11.1.71.21"
count = 0
stringBuilder = ''
segments = 1

for i in range(0, len(ipAddress)):
    if ipAddress[i] == ".":
        print("There are {} digits in {}".format(count, stringBuilder))
        count = 0
        stringBuilder = ''
        segments += 1
    else:
        count += 1
        stringBuilder += ipAddress[i]

# Since no dots are left, print updated variable on what's left at the end of the IP.
print("There are {} digits in {}".format(count, stringBuilder))

print()
print("{} total segments are in {}".format(segments, ipAddress))


# ALTERNATE SOLUTION

# # ipAddress = input("Enter an IP address: ")
# ipAddress = "123.232.22.1723"
# segment = 1
# length = 0
#
# for character in ipAddress:
#     if character == ".":
#         print("Segment {} contains {} characters.".format(segment, length))
#         segment += 1
#         length = 0
#     else:
#         length += 1
#
# # unless final character in string was a . then we haven't printed last segment
# # Print final values for last few digits
# print("Segment {} contains {} characters.".format(segment, length))