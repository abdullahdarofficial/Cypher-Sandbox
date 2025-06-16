class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        seen = {}  # To store number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
