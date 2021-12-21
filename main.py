hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

sumOfPrices=0
for x in prices:
  sumOfPrices = x + sumOfPrices
print(sumOfPrices)

averagePrice = sumOfPrices / len(prices)
print('Average Haircut Price: $'+ str(round(averagePrice,2)))

newPrices = [x -5 for x in prices]
print(newPrices)

totalRev = 0
for i,x in enumerate(prices):
  totalRev = totalRev + x*last_week[i]

print(totalRev)

dailyRevAverage = totalRev / 7
print(dailyRevAverage)

under30 = [newPrices[x] for x in range(len(newPrices)-1) if newPrices[x] < 30]
print(under30)

nums = [i for i in range(1,1001) if '6' in str(i)]
print(nums)
#this is just some practice with list comprehension 
#prints all numbers from 1-1000 that contain a 6
nums = [i for i in range(1,1001) if i%8==0]
print(nums)
#prints all numbers from 1-1000 that are divisible by 8