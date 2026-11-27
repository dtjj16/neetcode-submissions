import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        f = {}        
        heap = []
        for task in tasks:
            f[task] = f.get(task, 0) + 1
        for task, freq in f.items():
            heapq.heappush_max(heap, (freq, task))
        
        curr_turn = 0
        q = deque() 

        #heap is for processing tasks with highest frequency greedily
        #the queue is to enforce cooldown
        #every turn, check if we can add more elements into the heap 
        #queue node: (next available time, (freq, task))

        while heap or q:
            while q and q[0][0] <= curr_turn:
                heapq.heappush_max(heap, q[0][1])
                q.popleft()

            if heap:
                (freq, task) = heapq.heappop_max(heap)
                #append 
                if freq - 1 > 0:
                    q.append((curr_turn + n + 1, (freq - 1, task)))
                curr_turn += 1
            else: #if heap is empty, and nothing in queue can be ppopped -> remain idle, fast forward 
                curr_turn = q[0][0]
        return curr_turn
            
            
        

            











        