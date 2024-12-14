import percentages
import validator

percentages1 = [25, 50, 10, 15]
x = validator.validatePercentages(percentages1)
#percentages.print1()
if x:
    print("The values work")
else:
    print("The values don't work")

print (percentages.findGCF([24,12,6,3]))
print (percentages.findLCM([24,12,6,3]))

money = [14, 21]
targetPercentages = [50, 50]

print (percentages.findNumBills(money, targetPercentages))
