# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        
        # return (rand7() + rand7()) % 11

        while True:
            # Generate a number in the range [1, 49]
            num = (rand7() - 1) * 7 + rand7()  # This gives us a number between 1 and 49
            if num <= 40:
                # Map num to [1, 10]
                return (num - 1) % 10 + 1  # This gives us a uniform number between 1 and 10