class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Base check for same characters and length
        if len(set(s)) != len(set(t)) or len(s) != len(t):
            return False
        
        s_sorted = sorted(s)
        l_sorted = sorted(t)
        for i in range(len(s_sorted)):
            if s_sorted[i] != l_sorted[i]: 
                return False

        return True