import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        al_num = ''.join(char for char in s if char.isalnum()).lower()
        l, r = 0, len(al_num) - 1

        while l < r:
            if al_num[l] != al_num[r]:
                return False
            l += 1
            r -= 1
        return True