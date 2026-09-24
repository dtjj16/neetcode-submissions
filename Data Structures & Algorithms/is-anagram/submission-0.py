class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        #can either have two hashmaps and do equality 
        #how do i do it in one pass? add to count for s, subtract for t  
        if len(s) != len(t):
            return False
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1

        for char in t:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] -= 1
        
        for k, v in hashmap.items():
            print(k, v)
            if v != 0:
                return False 
        
        return True 