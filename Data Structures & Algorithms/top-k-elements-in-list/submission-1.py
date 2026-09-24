import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary, num: count
        # sorted(dict.items, key = lambda x: x[1])
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        # sorted_vals = sorted(d.items(), key=lambda x: x[1], reverse=True) #sorted by count
        # res = []
        # for i in range(k): 
        #     res.append(sorted_vals[i][0])
        # return res

        heap = [(count, num) for num, count in d.items()]
        heapq.heapify_max(heap)
        res = []
        for i in range(k): 
            res.append(heapq.heappop_max(heap)[1])
        return res


