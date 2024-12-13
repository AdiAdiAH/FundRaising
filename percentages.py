bills = [21, 14, 12, 18, 3, 31, 29]
alist = [14, 21]
blist = [50, 50]
percentages = [6.84, 15.75, 25.68, 3.59, 4.96, 4.10, 39.08]
print("Hello, World")
def validatePercentages(percentageList):
    sum = 0
    for i in range(0 ,len(percentageList)):
        sum += percentageList[i]
    if sum == 100:
        return True
    else:
        print(sum)
        return False
def convertP(percentageList):
    newPercentages = []
    for i in range(0, len(percentageList)):
        newPercentages.append(int(percentageList[i] * 100))
    return newPercentages

def findGCF(x, y):
    while x > 0:
        r = y % x
        y = x
        x = r
    return y

def findBigGCF(list):
    c = list[0]
    for i in range(1, len(list)-1):
        c = findGCF(c, list[i])
    return c

def LCM(list):
    lcm = 1
    for i in list:    
        lcm = lcm * i // findGCF(lcm, i)
    return lcm

def findNumBills(m, r):
    numList = []
    newS = []
    s = convertP(r)
    g = findBigGCF(s)
    for x in range(0, len(s)):
        newS.append(s[x] / g)
    c = LCM(m)
    for i in range(0, len(m)):
        n = c*(newS[i]/m[i])
        numList.append(int(n))
    return numList
if __name__ == "__main__":
    
    x = validatePercentages(percentages)
    if x:
        print("The following values add to 100")
    else:
        print("The following values do not add to 100")
    def print1():
        print("Aditya Ram")
    print1()
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