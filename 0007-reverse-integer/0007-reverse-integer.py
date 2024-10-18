class Solution:
    def reverse(self, x: int) -> int:
        
        # isNeg = False
        # if x < 0:
        #     isNeg = True
        #     x = -1 * x
        # val = 0
        # count = 0
        # l = []
        # while x > 0:
        #     l.append(x % 10)
        #     x//=10
        # while l:
        #     rem = l.pop()
        #     val = val + rem * (10 ** count)
        #     count += 1
        # if isNeg:
        #     val = -1 * val
        # num = val
        # print(num)
        # if num < -2147483648 or num > 2147483647:
        #     return 0
        # return num

        # Handle sign
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the integer
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # Apply the sign
        reversed_num *= sign
        
        # Check for overflow (32-bit signed integer range)
        if reversed_num < -2147483648 or reversed_num > 2147483647:
            return 0
        
        return reversed_num