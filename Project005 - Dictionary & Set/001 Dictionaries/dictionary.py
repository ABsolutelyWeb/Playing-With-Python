fruit = {"orange": "an orange, citric fruit.",
         "apple": "a crunchy, sweet fruit.",
         "lime": "a green, sour fruit.",
         "watermelon": "big, green fruit, pink inside."}

# print(fruit)
# print(fruit["lime"])


# add to dictionary
fruit["avocado"] = "Green fruit with big seed inside."
print(fruit)
fruit["avocado"] = "Can make guacamole."
print(fruit)


# delete from dictionary
# del fruit
del fruit["lime"]
print(fruit)


# empty dictionary
# fruit.clear()


# check if fruit exists
# while True:
#     dict_key = input("Enter a fruit: ")
#     if dict_key == "q" or dict_key == "quit":
#         print("bye")
#         break
#     # do in two lines what the below if/else statement is doing
#     desc = fruit.get(dict_key, "Don't have {}.".format(dict_key))
#     print(desc)
#     # if dict_key in fruit:
#     #     desc = fruit.get(dict_key)
#     #     print(desc)
#     # else:
#     #     print("Don't have {}".format(dict_key))



# print everything in dictionary one by one
# for fruity in fruit:
#     print(fruity + ": " + fruit[fruity])



# print dictionary 10 times to see if order changes
# for i in range(10):
#     for snack in fruit:
#         print(snack + ": " + fruit[snack])
#         print()



# make dictionary ordered by taking the result and storing in list and then sorting it.
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
ordered_keys = sorted(list(fruit.keys()))    # Does what the above 2 lines do.
for f in ordered_keys:
    print(f + " - " + fruit[f])

# OR do it in two lines
# for f in sorted(fruit.keys()):
#     print(f + " : " + fruit[f])



