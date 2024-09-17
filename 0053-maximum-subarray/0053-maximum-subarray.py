# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         left = 0
#         max_sum = max(nums)
#         curr = 0

#         for right in range(len(nums)):
#             if curr + nums[right] <= 0:
#                 curr = 0
#                 left = right + 1
#             else:
#                 curr += nums[right]
#                 max_sum = max(curr, max_sum)

#         return max_sum
            


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum = curr_sum = nums[0]
        
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
