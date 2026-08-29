class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Base check for same characters and length
        if len(set(s)) != len(set(t)) or len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] in s_dict.keys():
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 0

            if t[i] in t_dict.keys():
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 0
        print(s_dict)
        print(t_dict)
        return s_dict == t_dict