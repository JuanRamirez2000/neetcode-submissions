class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Base check to see if they are the same length
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
                continue
            s_dict[letter] = 1
        
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
                continue
            t_dict[letter] = 1

        return True if s_dict == t_dict else False
        # sorting approach O(n*logn) time O(n) space
        # sorted_s = ''.join(sorted(s))
        # sorted_t = ''.join(sorted(t))
        # return True if sorted_s == sorted_t else False