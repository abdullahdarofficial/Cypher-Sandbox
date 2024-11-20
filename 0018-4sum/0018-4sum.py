class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # n = len(nums)
        # if n < 4:
        #     return []
        
        # nums = sorted(nums)
        # result = set()
        
        # # Basic solution O(n^4)
        # for i in range(n - 3):
        #     for j in range(i + 1, n - 2):
        #         for k in range(j + 1, n - 1):
        #             for l in range(k + 1, n):
        #                 if (nums[i] + nums[j] + nums[k] + nums[l]) == target:
        #                     result.add((nums[i], nums[j], nums[k], nums[l]))

        # return [x for x in result]

        n = len(nums)
        if n < 4:
            return []
        
        nums = sorted(nums)
        result = set()
        
        for i in range(n - 3):
            for j in range(n - 1, i + 2, -1):
                
                k = i + 1
                l = j - 1
                while k < l:
                    currsum = nums[i] + nums[j] + nums[k] + nums[l]
                    if currsum > target:
                        l -= 1
                    elif currsum < target:
                        k += 1
                    else:
                        result.add((nums[i], nums[j], nums[k], nums[l]))
                        l -= 1
                        k += 1

        return [x for x in result]
