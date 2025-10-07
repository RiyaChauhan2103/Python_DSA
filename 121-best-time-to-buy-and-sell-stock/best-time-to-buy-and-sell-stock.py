class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit=max(prices)-min(prices)
        # # for i in range(0,len(prices)):
        # #     for j in range(i,len(prices)):
        # #         diff=prices[j]-prices[i]
        # #         max_profit=max(diff,max_profit)
        
        # return max_profit if max_profit>0 else 0
        # with kadane algorithm
        if not prices: 
            return 0
        curr=max_profit=0
        for i in range(1,len(prices)):
            profit=prices[i]-prices[i-1]
            # print(profit)
            curr=max(0,profit+curr)
            max_profit=max(curr,max_profit)
        return max_profit
        # return max(prices)-min(prices)