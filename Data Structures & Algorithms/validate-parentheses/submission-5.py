class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        matched_pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []    
        for char in s:
            if char not in matched_pairs:
                stack.append(char)
                continue

            if char in matched_pairs:
                if len(stack) == 0:
                    return False
                if matched_pairs[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) > 0:
            return False
        return True