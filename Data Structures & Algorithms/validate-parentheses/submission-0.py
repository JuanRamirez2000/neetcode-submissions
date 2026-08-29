class Solution:
    def isValid(self, s: str) -> bool:
        Map = {')': '(', ']': '[', '}': '{'}
        final = []
        for char in s:

            #If the character isnt a closing tag
            #Add it to the stack
            if char not in Map:
                final.append(char)
                continue

            #if final is empty or the characers done match
            if not final or final[-1] != Map[char]:
                return False

            final.pop()        

        return not final