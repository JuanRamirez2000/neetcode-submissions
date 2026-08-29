class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        w1 = [char for char in word1]
        w2 = [char for char in word2]

        left = right = 0

        while left < len(w1) and right < len(w2):
            ans.append(w1[left])
            ans.append(w2[right])
            left += 1
            right += 1
        
        while left < len(w1):
            ans.append(w1[left])
            left += 1

        while right < len(w2):
            ans.append(w2[right])
            right += 1
        
        return "".join(ans)