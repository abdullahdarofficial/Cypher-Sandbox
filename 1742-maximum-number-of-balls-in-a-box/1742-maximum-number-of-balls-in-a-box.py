class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def numsum(x):
            result = 0
            while x > 0:
                result += x%10
                x//=10
            return result

        maxcount = float('-inf')
        map = {}
        for num in range(lowLimit, highLimit + 1):
            boxNum = numsum(num)
            print(boxNum)
            if boxNum not in map:
                map[boxNum] = 0
            map[boxNum] += 1
            maxcount = max(map[boxNum], maxcount)

        return maxcount
            
            
