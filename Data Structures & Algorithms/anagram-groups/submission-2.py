class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Puts everything into a dict where keys are the strings
        final_dict = defaultdict(list)

        for string in strs:
            #Sort the string
            sorted_string = ''.join(sorted(string))

            #if there is a hit then add the string to that sorted value
            #This works because as you go along any hit is based on a sorted string
            #If two strings are anagrams and they are sorted then they are the same string
            final_dict[sorted_string].append(string)

        return list(final_dict.values())


        # The below solution builds off of isAnagram
        # https://neetcode.io/problems/is-anagram
    #     final_result = []
    #     for string in strs:
    #         current = []
    #         for other in strs:
    #             if self.isAnagram(string, other):
    #                 current.append(other)
    #         final_result.append(current)

    #     return [list(i) for i in set(map(tuple, final_result))]


    # def isAnagram(self, s: str, t:str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     s_dict = {}
    #     t_dict = {}
    #     for letter in s:
    #         if letter in s_dict:
    #             s_dict[letter] += 1
    #             continue
    #         s_dict[letter] = 1
        
    #     for letter in t:
    #         if letter in t_dict:
    #             t_dict[letter] += 1
    #             continue
    #         t_dict[letter] = 1

    #     return True if s_dict == t_dict else False