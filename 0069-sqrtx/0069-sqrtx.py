class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 1
        while i <= x:

            if (i * i) >= x:
                if (i * i) == x:
                    return i
                return i - 1
            i += 1
        return 0
