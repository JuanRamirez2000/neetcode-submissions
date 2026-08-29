import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = re.sub(r'[\W_]+', '', s).lower().replace(" ", "") 

        filtered_rev = filtered[::-1]
        for i in range(len(filtered)):
            if filtered[i] != filtered_rev[i]:
                return False

        return True