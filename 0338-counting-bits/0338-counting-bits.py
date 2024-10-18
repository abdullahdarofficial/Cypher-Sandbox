class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def makeBinary(num):
            count = 0
            while num > 0:
                if num % 2 != 0:
                    count += 1
                num //= 2

            return count

        return [makeBinary(x) for x in range(n + 1)]

        