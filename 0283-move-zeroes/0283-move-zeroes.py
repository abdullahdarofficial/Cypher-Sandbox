class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        # slow = 0
        # while slow < len(nums):
        #     if nums[slow] == 0:
        #         fast = slow + 1
        #         if fast < len(nums) and nums[fast] == 0:
        #             fast += 1
        #         if fast == len(nums):
        #             break
        #         nums[slow], nums[fast] = nums[fast], nums[slow]
        #     slow += 1
        #     print(nums)

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        