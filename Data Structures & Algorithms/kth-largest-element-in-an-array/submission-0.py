import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #maintain heap size of k
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]