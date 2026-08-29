class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_result = []
        for string in strs:
            current = []
            for other in strs:
                if self.isAnagram(string, other):
                    current.append(other)
            final_result.append(current)
        return [list(i) for i in set(map(tuple, final_result))]


    def isAnagram(self, s: str, t:str) -> bool:
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