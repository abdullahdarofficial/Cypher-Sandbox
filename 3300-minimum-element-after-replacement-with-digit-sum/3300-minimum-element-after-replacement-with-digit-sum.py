class Solution:
    def minElement(self, nums: List[int]) -> int:

        def sumNum(n):
            s = []
            while n > 0:
                s.append(n%10)
                n//=10
            res = 0
            for num in s:
                res += int(num)
            return res
        


        minres = float('inf')
        for i in range(len(nums)):
            minres = min(sumNum(nums[i]), minres)
        return minres


