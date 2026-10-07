class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #i want to expand the window only if next elem == curr elem
        #else reset counter, left and right pointers to same next position
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        curr = set()    
        max_len = -1
        curr_len = 0
        l = 0
        for r in range(len(s)):

            while s[r] in curr:
                #if we encounter a duplicate, it means that we need to move the window till duplicated char index + 1
                curr.remove(s[l])
                l += 1
                curr_len -= 1 
            #s[r] is still unique 
            curr.add(s[r])
            curr_len += 1
            max_len = max(max_len, curr_len)
        return max_len


