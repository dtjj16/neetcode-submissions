import heapq 

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # node is (frequency, number), and i heapify this, and then pop k times. 
        count = {}
        heap = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for n, c in count.items():
            heapq.heappush(heap, (-c, n)) #negate count because we want max freq
        res = []
        for i in range(k):
            value = heapq.heappop(heap)[1]
            res.append(value)
        return res
