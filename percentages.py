bills = [21, 14, 12, 18, 3, 31, 29]
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
    
convertP(percentages)
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
def findGCF(x, y):
    while x > 0:
        r = y % x
        y = x
        x = r
    return y

def findBigGCF(list):
    for i in range(0, len(list))
    findGCF(list[i], list[i+1])
         
#print(findGCF(3084, 1424)) 

findBigGCF(convertP(percentages))  

if __name__ == "__main__":
    
    x = validatePercentages(percentages)

    if x:
        print("The following values add to 100")
    else:
        print("The following values do not add to 100")
    def print1():
        print("Aditya Ram")
    print1()
