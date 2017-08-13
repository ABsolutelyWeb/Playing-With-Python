# TUPLES

# Are immutable which means they cannot be changed.
# Appending something to a tuple would yield in an error.


# =================== TEST 1: Intro to tuples

# t = "a", "b", "C"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))   # Double parentheses signify a tuple.




# =================== TEST 2:

msg = "The Fantastic ", "Four", 4
msg2 = "Battlefield", "Bad Company", 2
msg3 = "Harry Potter", "Sorcerer Stone", 4

# msg2[0] = "The Fan4stic"         # Does not work because tuples are immutable.
# msg2 = msg2[0], "BURP", msg2[2]     # Instead, we can change values like this.
# print(msg2)
# print(msg2[0])
# print(msg2[1])
# print(msg2[2])


# Unpacking tuple
# title, subtitle, quantity = msg
# print(title)
# print(subtitle)
# print(quantity)


# Tuple within a tuple
# msg4 = "Captain", "Underpants", 20, (("And", "The", 4), ("Revenge", "of", 3))
# print(msg4)
#
# title, artist, year, tracks = msg4
#
# print(title)
# print(artist)
# print(year)
# print(tracks)




# CHALLENGE: Take the imelda tuple, print out the album along with all tracks.
# Indent each track with a tab.

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

title, artist, year, tracks = imelda

print("{0} by {1} from {2}".format(title, artist, year))

# for items in tracks:
#     print("\tTrack Number {0}. {1}".format(items[0], items[1]))

for items in tracks:
    track, title = items
    print("\t Track {}, Title: {}".format(track, title))