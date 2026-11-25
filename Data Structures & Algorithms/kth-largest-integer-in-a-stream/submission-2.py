import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums = nums
        heapq.heapify(self.nums)
        self.k = k
    
    #maintain heap of size k
    #the head (min value) will be the k-th largest element 
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]


            



