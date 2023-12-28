#Input: prices = [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

prices1=[7,1,5,3,6,4]
prices2=[7,6,4,3,1]

def Stock(prices):
    mini=prices[0]
    profit=0
    for i in range(1,len(prices)):
        cost=prices[i]-mini
        profit=max(profit,cost)
        mini=min(mini,prices[i])
    return profit
print(Stock(prices1))
print(Stock(prices2))