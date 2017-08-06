#! python3

# first = "You ran "
# count = 7
# second = " times!"
# print(first + str(count) + second)
#
#
# # print("Type something: ")
# # third = input()
# # print("You typed \"" + str(third) + "\"")
#
# for i in range(1, 6):
#     print(i)
#
# cockatoo = "Umbrella Cockatoo"
# print(cockatoo[0:8])
# print("Cockatoo" in cockatoo)
# print(len(cockatoo[0:8]))
#
#
# name = input("What is your name?: ")
# age = int(input("How old are you, {0}?: ".format(name)))
#
# if age >= 18 and age < 100:
#     print("You are " + str(age) + " years old and old enough to vote.")
# elif age >= 100:
#     print("You should be dead!")
# else:
#     print("You are too young. Come back in {0} years.".format(18-age))





name = input("What is your name?: ")
age = int(input("What is your age, {0}?: ".format(name)))

if 18 <= age <= 30:
    print("Welcome to the holiday, {0}.".format(name))
else:
    print("Sorry, {0}, but you do not meet the age requirement.".format(name))
