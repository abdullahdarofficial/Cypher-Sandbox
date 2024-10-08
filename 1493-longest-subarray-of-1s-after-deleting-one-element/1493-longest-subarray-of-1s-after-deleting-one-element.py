class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # index = -1
        # left = 0
        # maxcount = 0
        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         if index == -1:
        #             index = right
        #         else:
        #             left = index + 1
        #             index = right
        #     else:
        #         maxcount = max(maxcount, right - left)
        # return maxcount - 1 if index == -1 else maxcount


        left = 0
        maxCount = 0
        zeroCount = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeroCount += 1

            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            maxCount = max(maxCount, right - left)

        return maxCount