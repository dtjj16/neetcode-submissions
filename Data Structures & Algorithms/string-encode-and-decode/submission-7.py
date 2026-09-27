class Solution:

    def encode(self, strs: List[str]) -> str:
        #naive solution to introduce delimiters between each string,
        #particularly a non ascii char, but we can take it further by including length
        encoded = ""
        for string in strs:
            n = len(string)
            delim = str(len(string)) + "#"
            encoded = "".join([encoded, delim, string])
        return encoded
        

    def decode(self, s: str) -> List[str]:
        #it has to process digits first, until it reaches '#', 
        #int version of the digit represents length of string to process
        tmp = [] #this will hold current length to process
        curr_str = []
        res = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                tmp.append(s[i])
                i += 1
            elif s[i] == '#':
                #process tmp, reset vars
                length = int("".join(tmp))
                for j in range(i+1, i+1+length):
                    curr_str.append(s[j])
                res.append("".join(curr_str))
                tmp = []
                curr_str = []
                i = i + 1 + length
        return res
    
        
