# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         while x >= 10:
#             num = 1
#             count = 0
#             while (x // num) > 0:
#                 num *= 10
#             num //= 10
#             x1 = x % 10
#             x2 = x // num

#             print(x1, x2)
#             if x1 != x2:
#                 return False
            
#             x -= num * x2
#             print(x)

#             x //= 10
#             print(x)

#         return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and multiples of 10 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Initialize variables
        original = x
        reversed_half = 0
        
        while x > 0:
            # Extract the last digit and build the reversed_half
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Compare original number with reversed_half
        return original == reversed_half
