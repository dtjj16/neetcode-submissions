class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We can use the sliding window approach. The window size will  
        # be dynamic, and we will shrink the window when the number of 
        # replacements exceeds k. The result will be the maximum window 
        # size observed at each iteration.

        left = 0 #index positions
        freq_map = {}
        longest_ss = 0
        curr_max_freq = 0

    # Consider starting with an empty map and a window that hasn’t      included anything yet, so the loop body handles adding the new character the same way every time. Ask yourself: what’s the first thing that should happen when right advances?

        for right in range(len(s)):
            #move right when curr_len - curr_max_freq <= k
            #or move left when curr_len - curr_max_freq > k
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1
            curr_max_freq = max(curr_max_freq, freq_map[s[right]])
            
            #curr_len = right - left + 1
            while (right - left + 1) - curr_max_freq > k:
                #left shift
                freq_map[s[left]] = freq_map.get(s[left], 0) - 1
                left += 1 

           #longest substring is max_freq + k == curr_len
            longest_ss = max(longest_ss, (right - left + 1))
        return longest_ss

#XXXYXYY YY
# XXYXYYY Y

