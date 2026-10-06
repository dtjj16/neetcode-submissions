"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if len(intervals) == 0:
            return 0
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        
        starts.sort()
        ends.sort()

        # the idea is looking at each point chronologically 
        count = 0
        max_count = -1
        condition = True
        start_pointer = 0
        end_pointer = 0
        while condition:
            if starts[start_pointer] < ends[end_pointer]:
                #take smaller value first
                count += 1
                max_count = max(max_count, count)
                start_pointer += 1

            elif starts[start_pointer] == ends[end_pointer] or starts[start_pointer] > ends[end_pointer]:
                count -= 1
                end_pointer += 1

            # start times will always complete before end times 
            if start_pointer == len(starts):
                return max_count

        return max_count


