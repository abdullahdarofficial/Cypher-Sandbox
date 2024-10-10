class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # if not nums or len(nums) == 1:
        #     return 0
        # if len(nums) == 2:
        #     return 0 if nums[0] > nums[1] else 1
        # left = 1
        # right = len(nums) - 2

        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid - 1] < nums[mid] > nums[mid + 1]:
        #         return mid
        #     elif nums[mid - 1] > nums[mid]:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
             
        # return 0 if nums[0] > nums[-1] else len(nums) - 1

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left