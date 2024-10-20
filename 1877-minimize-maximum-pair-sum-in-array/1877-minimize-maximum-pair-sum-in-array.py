class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()

        currmax = 0
        size = len(nums)
        for i in range(size // 2):
            currmax = max(currmax, nums[i] + nums[size - 1 - i])


        return currmax
        