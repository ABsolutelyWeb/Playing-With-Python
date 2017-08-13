from random import randint


# We will execute randint (between -1 and 1 inclusive) n number of times (whatever 'executions' equals).
# Each time we will add the x to total sum and then divide the number by total executions. The Law of
# Large Numbers states that if we are taking the average of a set of numbers, the average will be closer
# to what we expect if we increase sample size. So the larger the number of executions, the closer the
# average will be to our expected average. Our expected average over a range of -1, 0, 1 is 0. So the
# larger the executions, the closer we will get to zero.

totalSum = 0
executions = int(input("How many random integers should we generate?: "))
temp = executions
while executions > 0:
    x = randint(-1, 1)
    if -1 < x < 1:
        totalSum = x + totalSum
    executions = executions - 1
if totalSum == 0:
    print("Could not print average.")
else:
    print("{}".format(totalSum/temp))
print("We ran " + temp + " exections.")

