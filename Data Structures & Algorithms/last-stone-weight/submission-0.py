import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)
        while len(heap) > 1:
            x = heapq.heappop_max(heap)
            y = heapq.heappop_max(heap)
            if x == y:
                continue
            elif x < y:
                new_stone = y - x
                heapq.heappush_max(heap, new_stone)
            elif y < x:
                new_stone = x - y
                heapq.heappush_max(heap, new_stone)
        if heap:
            return heap[0]
        return 0        
        
            
