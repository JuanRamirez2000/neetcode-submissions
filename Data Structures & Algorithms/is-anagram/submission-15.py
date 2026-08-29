from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_d = defaultdict(int)
        t_d = defaultdict(int)

        for char in s:
            s_d[char] += 1
        
        for char in t:
            t_d[char] += 1
        
        return s_d == t_d