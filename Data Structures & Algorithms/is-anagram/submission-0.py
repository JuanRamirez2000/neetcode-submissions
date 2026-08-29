class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base check to see if they are the same length
        if len(s) != len(t):
            return False
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))
        for a,b in zip(sorted_s, sorted_t):
            if a != b:
                return False
        return True