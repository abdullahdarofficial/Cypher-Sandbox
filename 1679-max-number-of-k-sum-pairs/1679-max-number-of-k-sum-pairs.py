class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        if not nums:
            return 0
        nums.sort()

        start = 0 
        end = len(nums) - 1
        counter = 0

        while start < end:
            if nums[start] + nums[end] == k:
                counter += 1
                start += 1
                end -= 1
            elif nums[start] + nums[end] < k:
                start += 1
            elif nums[start] + nums[end] > k:
                end -= 1
         
        return counter
