class Solution:
    def reverseBits(self, n: int) -> int:
        
        # result = []
        # while n > 0:
        #     if n % 2 == 0:
        #         result.append('0')
        #     else:
        #         result.append('1')
        #     n //= 2

        # while(len(result) < 32):
        #     result.append('0')
        # print(result)

        # n = 0
        # for i in range(len(result)):
        #     if result[31 - i] == "1":
        #         n += 2 ** i
        # return n

        result = 0
        for i in range(32):
            # Shift result to the left to make space for the next bit
            result <<= 1
            # Extract the rightmost bit of n and add it to result
            result |= n & 1
            # Shift n to the right to process the next bit
            n >>= 1
        return result