class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        d = {}
        for s in strs:
            tmp = "".join(sorted(s))
            if tmp in d:
                d[tmp].append(s)
            else:
                d[tmp] = [s]
        res = []
        for v in d.values():
            res.append(v)
        return res