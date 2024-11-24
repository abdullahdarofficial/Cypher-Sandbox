class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                index = i
                break
        if index != -1:
            nums[index:].sort()
        else:
            nums.sort()




