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

name = input("Give me your name: ")
age = int(input("Give me your age as an integer, {}: ".format(name)))

if (age >= 18) and (age < 31):
    print("Welcome to the holiday, {}.".format(name))
elif age > 30:
    print("Sorry, {}, but you are too old for this.".format(name))
else:
    print("Sorry, {}, but you are too young for this.".format(name))
