#######################################################################################################################


# ORGANIZATION A
# You have 2 lists of data: 1 for monthly revenue and the other for monthly expenses. Both for the year. Calculate the
# following metrics:
            # Profit for each month
                # SOLUTION:
                    # profitEachMonth(revenue, expenses)

            # Profit after tax each month (tax rate: 30%)
                # SOLUTION:
                    # profitEachMonth(revenue, expenses, .3)

            # Profit margin for each month (profit after tax / revenue)
                # SOLUTION:
                    # profitMarginPerMonth(revenue, expenses, .3)

            # Good months where profit after tax was greater than the mean.
                # SOLUTION:
                    # monthStatus(revenue, expenses, .3, "g")

            # Bad months where the profit after tax was less than the mean.
                # SOLUTION:
                    # monthStatus(revenue, expenses, .3, "b")

            # The best month where profit after tax was max.
                # SOLUTION:
                    # monthStatus(revenue, expenses, .3, "max")

            # The worst month where profit after tax was min.
                # SOLUTION:
                    # monthStatus(revenue, expenses, .3, "min")



# All results will be as lists.

# Dollar values must be calculated with $0.01 precision, but need to be presented in units of $1,000 (i.e. 1k) with no
# decimal points.

# Results for profit margin ratio need to be in units of % with no decimals.

# Negative tax is ok.


#######################################################################################################################


# Data
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97,
           15433.50]

expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37,
            3803.96]

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]


#######################################################################################################################


# Function to check lists for validity
def checkLists(list1, list2):

    # Check if both lists are equal in length. If not, throw error message.
    if len(list1) != len(list2):
        print("Inputted lists must be of equal length. Exiting...")
        return

    # Check if both lists are of type float.
    if not (all(isinstance(item, float) for item in list1)) or not (all(isinstance(item, float) for item in list2)):
        print("Both lists must be of type float. Exiting...")
        return

    print()
    print("List check complete. Proceeding with calculations...")
    print()


#######################################################################################################################


# Profit before taxes.
def profitBeforeTaxes(revenueList, expensesList):

    # Allocate an empty array to store the result.
    result = list()

    # Based on the average size of the two lists, loop that many times. Then subtract expenses
    # from revenue to get profit and append the value to the empty result list. Make sure all
    # results are two decimal places.
    for i in range(0, len(revenueList)):
        answer = round((revenueList[i] - expensesList[i]), 2)
        result.append(answer)

    return result


# Profit after taxes.
def profitAfterTaxes(revenueList, expensesList, taxRate):

    # Allocate an empty array to store the result.
    result = list()
    resultWithTax = list()

    for number in revenueList:
        taxedRevenue = (number - (number*taxRate))
        resultWithTax.append(taxedRevenue)

    for i in range(0, len(expensesList)):
        answer = round((resultWithTax[i] - expensesList[i]), 2)
        result.append(answer)

    return result



#######################################################################################################################


# Function for calculating profit for each month.
def profitEachMonth(revenueList, expensesList, taxRate=None):

    # Check list arguments.
    checkLists(revenueList, expensesList)

    if taxRate is None:
        print("No tax rate entered. Calculating profits per month before taxes.")
        result = profitBeforeTaxes(revenueList, expensesList)
        print()
        print("TOTAL PROFIT BEFORE TAXES")

    else:
        print("Tax rate of {} taken into effect for revenue.".format(taxRate))
        result = profitAfterTaxes(revenueList, expensesList, taxRate)
        print()
        print("TOTAL PROFIT AFTER TAXES")


    for i in range(0, len(result)):
        print("{0}: {1}".format(months[i], result[i]))


#######################################################################################################################


# (Profit after tax) / revenue
def profitMarginPerMonth(revenueList, expensesList, taxRate):

    checkLists(revenueList, expensesList)
    result = list()

    pAfterT = profitAfterTaxes(revenueList, expensesList, taxRate)
    for i in range(0, len(pAfterT)):
        answer = int(round((pAfterT[i] / revenueList[i])*100, 0))
        result.append(answer)

    for i in range(0, len(result)):
        print("{0}: {1}%".format(months[i], result[i]))


#######################################################################################################################


# Months where profit after tax > mean
def monthStatus(revenueList, expensesList, taxRate, monthType):

    checkLists(revenueList, expensesList)

    getIndex = list()

    sumTotal = 0
    pAfterT = profitAfterTaxes(revenueList, expensesList, taxRate)

    for number in pAfterT:
        sumTotal = sumTotal + number

    totalMean = sumTotal / len(pAfterT)
    print("Mean total is {}".format(totalMean))
    print()

    if monthType in ("good", "Good", "GOOD", "g"):
        for num in pAfterT:
            if num > totalMean:
                indexNum = pAfterT.index(num)
                getIndex.append(indexNum)
        print("GOOD MONTHS WERE:")

    elif monthType in ("bad", "Bad", "BAD", "b"):
        for num in pAfterT:
            if num < totalMean:
                indexNum = pAfterT.index(num)
                getIndex.append(indexNum)
        print("BAD MONTHS WERE:")

    elif monthType in ("max", "Max", "MAX"):
        maxVal = max(pAfterT)
        indexNum = pAfterT.index(maxVal)
        getIndex.append(indexNum)

    elif monthType in ("min", "Min", "MIN"):
        minVal = min(pAfterT)
        indexNum = pAfterT.index(minVal)
        getIndex.append(indexNum)

    print()
    for index in getIndex:
        print(months[index])


#######################################################################################################################

# MAIN PROGRAM (Uncomment to run the relevant function)

# profitEachMonth(revenue, expenses)
# profitEachMonth(revenue, expenses, .3)
# profitMarginPerMonth(revenue, expenses, .3)
# monthStatus(revenue, expenses, .3, "g")
# monthStatus(revenue, expenses, .3, "b")
# monthStatus(revenue, expenses, .3, "min")
# monthStatus(revenue, expenses, .3, "max")
