class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        
        # avg = sum(nums) // len(nums)

        # for i in range(len(nums)):
        #     if nums[i] <= avg:
        #         nums[i] += k
        #     else:
        #         nums[i] -= k

        # return max(nums) - min(nums)


        nums.sort()
        n = len(nums)
        result = nums[-1] - nums[0]

        for i in range(n - 1):
            max_val = max(nums[-1] - k, nums[i] + k)
            min_val = min(nums[0] + k, nums[i + 1] - k)
            result = min(result, max_val - min_val)

        return result