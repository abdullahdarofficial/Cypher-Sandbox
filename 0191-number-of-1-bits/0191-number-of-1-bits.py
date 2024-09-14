class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            # Check the rightmost bit using n & 1
            if n & 1:
                count += 1
            # Shift n to the right by 1 to check the next bit
            n >>= 1
        return count
