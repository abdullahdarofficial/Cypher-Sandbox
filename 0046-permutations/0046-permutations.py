class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def permutation(nums, curr):
            if len(nums) == 0:
                result.append(curr)
            else:
                for index, num in enumerate(nums):
                    permutation(nums[:index] + nums[index+1:], curr + [num])
        permutation(nums, [])
        return result