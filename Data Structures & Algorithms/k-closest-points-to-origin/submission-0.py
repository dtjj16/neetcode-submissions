import math
import heapq 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #maintain a max heap of size k (we want to pop large values)
        #for each cooordinate, calculate euclidean distance,
        #push into heap, pop when length > k 
        heap = []
        for p in points:
            x, y = p[0], p[1]
            dist = math.sqrt((x-0)**2 + (y-0)**2)
            node = (dist, p)
            heapq.heappush_max(heap, node)
            if len(heap) > k:
                heapq.heappop_max(heap)
        res = []
        for nodes in heap:
            res.append(nodes[1])
        return res


