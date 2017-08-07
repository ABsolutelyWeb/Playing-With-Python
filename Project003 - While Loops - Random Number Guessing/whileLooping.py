import random

#=================== TEST 1

# exits = ["east", "northeast", "south"]
# chosen = ""
#
# while chosen not in exits:
#     chosen = input("Choose a direction: ")
#     if chosen == "q":
#         print("GAME OVER")
#         break;
# else:
#     print("You got out!")


#=================== CHALLENGE

highest = 100
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest), end='')
guess = 0
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("bye")
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("CORRECT!")
        break
