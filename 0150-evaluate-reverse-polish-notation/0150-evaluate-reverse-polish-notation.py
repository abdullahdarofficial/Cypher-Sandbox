class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token != '+' and token != '-' and token != '*' and token != '/':
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                result = 0
                if token == '+':
                    result = num2 + num1
                elif token == '-':
                    result = num2 - num1
                elif token == '*':
                    result = num2 * num1
                elif token == '/':
                    result = num2 / num1
                
                stack.append(int(result))
            
        return stack.pop()
                
