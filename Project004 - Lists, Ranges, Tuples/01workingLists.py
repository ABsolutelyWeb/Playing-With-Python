# ######### TEST 1: count()

# ipAddress = input("Enter IP Address.")
# print(ipAddress.count("."))




# ######### TEST 2: Append()

# listOfCockatoos = ["moluccan", "goffins", "corella", "gallah", "black palm", "umbrella", "sulfur-crested"]
# listOfCockatoos.append("mjr mitchell's")
#
# for tooType in listOfCockatoos:
#     print("{} cockatoo".format(tooType))




# ######### TEST 3: Concatenating lists, sorting

# evenNum = [12, 14, 16, 18]
# oddNum = [13, 15, 17, 19, 21, 23, 25, 27]
#
# combine = evenNum + oddNum
# # combine.sort()        # Permanently changes combine
# print(sorted(combine))  # Temporarily changes combine




# ######### TEST 4: Creating lists with constructors

# # two ways to make / initialize an empty list.
# list1 = []
# list2 = list()
#
# # Create a list on the fly using the list constructor.
# print(list("The lists are equal."))




# ######### TEST 5: Reverse and more sorting

# # This updates evenNum AND another_evenNum
# evenNum = [22, 26, 30, 34, 38]
# another_evenNum = evenNum
# another_evenNum.sort(reverse=True)
# print(evenNum)
# print(another_evenNum)

# # To stop both lists from updating due to sort, we can modify code with following:
# evenNum = [22, 26, 30, 34, 38]
# another_evenNum = list(evenNum)
# another_evenNum.sort(reverse=True)
# print(evenNum)
# print(another_evenNum)

# # Another way.
# evenNum = [22, 26, 30, 34, 38]
# another_evenNum = sorted(evenNum, reverse=True)
# print(evenNum)
# print(another_evenNum)




# ######### TEST 6: List of lists and nested printed

# evenNum = [22, 26, 30, 34]
# oddNum = [23, 27, 31, 35, 39]
#
# # A list of two lists
# allNum = [evenNum, oddNum]
# print(allNum)
# print()
# for numbers in allNum:
#     print(numbers)
#     print()
#     for subNumbers in numbers:
#         print(subNumbers)




# ######### TEST 7: List of lists of food
# Print out the ingredients list of a combo that doesn't have spam.

# menu = []
# menu.append(["egg", "spam", "bacon"])
# menu.append(["egg", "sausage", "bacon"])
# menu.append(["egg", "spam"])
# menu.append(["egg", "bacon", "spam"])
# menu.append(["egg", "bacon", "sausage", "spam"])
# menu.append(["spam", "bacon", "sausage", "spam"])
# menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
# menu.append(["spam", "egg", "sausage", "spam"])
#
# # print(menu)
#
# for combo in menu:
#     if not "spam" in combo:
#         # print(combo)
#         for ingredients in combo:
#             print(ingredients)




# ######### TEST 8: Iterators

# stringNum = "1234567890"

# for char in stringNum:
#     print(char)

# Another way of iterating through a string.
# customIterator = iter(stringNum)
# print(customIterator)
# print(next(customIterator))
# print(next(customIterator))
# print(next(customIterator))
# print(next(customIterator))
# print(next(customIterator))
# print(next(customIterator))
# print(next(customIterator))
# print(next(customIterator))
# print(next(customIterator))
# print(next(customIterator))


# for char in stringNum:
#     print(char)
#
# # This example below is exactly what is happening
# # in the for loop directly above.
# for char in iter(stringNum):
#     print(char)

pc = ["motherboard", "RAM", "storage space", "CPU", "GPU", "PSU", "case", "CPU cooler", "cooling fans"]
customPCiterator = iter(pc)

for i in range(0, len(pc)):
    print(next(customPCiterator))
