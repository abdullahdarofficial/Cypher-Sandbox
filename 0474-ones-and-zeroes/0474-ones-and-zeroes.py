class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def countZeroOne(string):
            zero = 0
            one = 0
            for char in string:
                if char == '0':
                    zero += 1
                else:
                    one += 1

            return (zero, one)
        
        count = 0
        for s in strs:
            zeros, ones = countZeroOne(s)
            if zeros <= m and ones <= n:
                count += 1
        return count if count != len(strs) else count - 1
