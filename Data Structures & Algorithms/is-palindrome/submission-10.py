class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_string = [l.lower() for l in s if l.isalnum()]
        reversed_string = cleaned_string[::-1]

        return True if reversed_string == cleaned_string else False

        # Two pointers approach
        # finalString = [l.lower() for l in s if l.isalnum()]
        # for i in range(len(finalString) // 2):
        #     if (finalString[i] != finalString[-i - 1]):
        #         return False
        return True