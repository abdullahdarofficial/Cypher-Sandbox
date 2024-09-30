class Solution:
    def decodeString(self, s: str) -> str:
        
        # if not s:
        #     return None

        # stack = []
        # result = []
        # for char in s:
        #     if char != ']':
        #         stack.append(char)
        #     else:
        #         alp = stack.pop()
        #         substr = ""
        #         while alp != "[":
        #             substr += alp
        #             alp = stack.pop()
        #         times = int(stack.pop())
        #         substr *= times
        #         stack.append(substr[::-1])

        # print(stack)
        # return "". join(stack)


        if not s:
            return ""

        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                # Build the number (in case of multi-digit)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current string and number onto the stack
                stack.append(current_str)
                stack.append(current_num)
                # Reset for the next part
                current_str = ""
                current_num = 0
            elif char == ']':
                # Pop the number and string from the stack
                num = stack.pop()
                prev_str = stack.pop()
                # Repeat the current string and concatenate
                current_str = prev_str + current_str * num
            else:
                # Build the current string
                current_str += char

        return current_str        

        
        