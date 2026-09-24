class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i, n in enumerate(nums): 
            d[n] = i
        #iterate through nums and see if the target - nums[j] exists 
        #where i != j
        res = []
        for i in range(len(nums)):
            k = target - nums[i]
            if k in d:
                j = d[k]
                if j != i:
                    res.append(i)
                    res.append(j)
                    break
        res.sort()
        return res
        