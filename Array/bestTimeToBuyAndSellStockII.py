def maxProfit(self, prices):

    ans = 0

    for i in range(1, len(prices)):
        if prices[i] - prices[i - 1] > 0:
            ans+=(prices[i] - prices[i - 1])

    return ans