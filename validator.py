def validatePercentages(percentageList):
    sum = 0
    for i in range(0 ,len(percentageList)):
        sum += percentageList[i]
    if sum == 100:
        return True
    else:
        print(sum)
        return False
    
def validateBillCounts (billCounts, moneyDenominations, percentages):
    pass

