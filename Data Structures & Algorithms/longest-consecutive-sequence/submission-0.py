class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #check if (num - 1) does not exist in an array to identify head
        if nums == []:
            return 0
        nums_set = set(nums)   
        heads = []
        for num in nums:
            if (num - 1) not in nums_set:
                heads.append(num)
        seq_length = []
        for head in heads:
            tmp_head = head
            curr_length = 1 
            while (tmp_head + 1) in nums_set:
                tmp_head += 1
                curr_length += 1
            seq_length.append(curr_length)
        return max(seq_length)
        