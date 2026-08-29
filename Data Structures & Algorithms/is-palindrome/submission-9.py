class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalString = [l.lower() for l in s if l.isalnum()]
        for i in range(len(finalString) // 2):
            if (finalString[i] != finalString[-i - 1]):
                return False
        return True