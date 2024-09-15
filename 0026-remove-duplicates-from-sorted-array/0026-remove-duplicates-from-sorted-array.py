class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        i = 1  # Start i from the second element
        
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i
