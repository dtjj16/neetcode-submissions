class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #window: how big is the interval, when do i move the boundaries
        #o(n): do it in a single pass, with not sorting 
        #left < right, max(right - left)
        #keep track of the smallest on the left of the pointer
        #check current pointer value, update  
        max_profit = 0
        buying_price = prices[0]
        for i in prices[1:]:
            if i < buying_price:
                buying_price = i            
            else:
                curr_profit = i - buying_price
                max_profit = max(max_profit, curr_profit)
        return max_profit