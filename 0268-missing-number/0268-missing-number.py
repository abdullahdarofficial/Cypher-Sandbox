class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        ans = 0
        for i in range(len(nums) + 1):
            ans = ans ^ i

        for num in nums:
            ans = ans ^ num

        return ans

        