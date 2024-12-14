import validator

bills = [21, 14, 12, 18, 3, 31, 29]
percentages = [6.84, 15.75, 25.68, 3.59, 4.96, 4.10, 39.08]
print("Hello, World")

def convertP(percentageList):
    newPercentages = []
    for i in range(0, len(percentageList)):
        newPercentages.append(int(percentageList[i] * 100))
    gcf = findGCF (newPercentages)
    newPercentages = [p / gcf for p in newPercentages]
    return newPercentages

def findGCF2(x, y):
    while x > 0:
        remainder = y % x
        y = x
        x = remainder
    return y

def findGCF(list):
    c = list[0]
    for i in range(1, len(list)):
        c = findGCF2(c, list[i])
    return c

def findLCM(list):
    lcm = 1
    for newNum in list:    
        lcm = lcm * newNum // findGCF2(lcm, newNum)
    return lcm

def findNumBills(moneyDenominations, percentages):
    billCounts = []
    ratio = convertP(percentages)
    moneyLCM = findLCM(moneyDenominations)
    for idx in range(0, len(moneyDenominations)):
        count = moneyLCM * (ratio[idx]/moneyDenominations[idx])
        billCounts.append(int(count))
    return billCounts

if __name__ == "__main__":
    
    x = validator.validatePercentages(percentages)
    if x:
        print("The following values add to 100")
    else:
        print("The following values do not add to 100")
    def print1():
        print("Aditya Ram")
    print1()
    
    alist = [14, 21]
    blist = [50, 50]

    print(findNumBills(alist, blist))

'''
def findGCF(x, y):
    if x <= y:
        n = x
        while True:
            if y % n == 0:
                break
            else:
                n -= 1
        print(n)
    else:
        n = y
        while True:
            if x % n == 0:
                break
            else:
                n -= 1
        print(n)
'''