class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums)
        newnums = nums + nums
        maxsum = float("-inf")
        for i in range(n):
            for j in range(i, n * 2):
                if j - i < n:
                    currsum = sum(newnums[i:j+1])
                    maxsum = max(maxsum, currsum)
        return maxsum

