class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        # count = 0
        # left = 0
        # subarr = []
        # for right in range(left + 1, len(nums) + 1):
        #     subarr = nums[left : right]
        #     print(subarr, count)
        #     if math.prod(subarr) < k:
        #         count += 1
        #         print("if", count)
        #     else:
        #         left += 1

        # while left < len(nums):
        #     left += 1
        #     if math.prod(nums[left:]) < k:
        #         count += 1
        #         print("if", count, nums[left:])

        # return count

        if k <= 1:
            return 0

        count = 0
        product = 1
        left = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k and left <= right:
                product //= nums[left]
                left += 1

            # Add all subarrays ending at `right`
            count += right - left + 1

        return count