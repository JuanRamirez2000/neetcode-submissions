class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{' 
        }
        stack = []
        for char in s:
            if char in pairs.values():
                stack.append(char)
                continue
            
            if char == ']':
                if len(stack) == 0:
                    return False
                elif stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False

            if char == '}':
                if len(stack) == 0:
                    return False
                elif stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False

            if char == ')':
                if len(stack) == 0:
                    return False
                elif stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False

        return(len(stack) == 0)