class Solution:
    def isValid(self, s: str) -> bool:

        #Base case
        if len(s) == 1:
            return False
        
        stack = []
        legend = {
            ')': '(',
            '}': '{',
            ']': '['
        }


        for char in s:

            #If it is not a closing bracket
            if char not in legend:
                stack.append(char)
                continue

            if char in legend:
                if len(stack) == 0:
                    return False
                if legend[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0