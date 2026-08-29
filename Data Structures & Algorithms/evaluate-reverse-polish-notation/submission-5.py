class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']

        stack = []
        for n in tokens:
            print(stack)
            if n not in operations:
                stack.append(int(n))
                continue
            
            if n in operations:
                if n == '+':
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(int(left + right))
                elif n == '-':
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(int(left - right))
                elif n == '*':
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(int(left * right))
                elif n == '/':
                    right = stack.pop()
                    left = stack.pop()
                    stack.append(int(left / right))
        return stack[0]