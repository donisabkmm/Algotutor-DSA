"""
2. Best Time to Buy and Sell Stock
You are given an array of prices where prices[i] is the price of a
given stock on an ith day.
You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day in the future to sell that
stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
profit = 6-1 = 5.
"""

testcases = [{"prices":[7,1,5,3,6,4]},
             {"prices":[9,6,1,5,4,3]},
             {"prices":[7,6,4,3,1]}]



class profit:
    def max_profit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

model = profit()


for i in range(len(testcases)):
    prices=testcases[i]["prices"]
    print(model.max_profit(prices=prices))
