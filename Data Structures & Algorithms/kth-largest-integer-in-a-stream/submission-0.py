class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        new_lst = sorted(self.nums, reverse=True)
        print(new_lst)
        c = 1
        for i in new_lst:
            if c == self.k:
                return i
            c += 1
        
            



