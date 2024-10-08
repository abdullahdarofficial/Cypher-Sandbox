class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # counter = 0
        # count = 0
        # indexes = set()
        # start = 0
        # maxcount = 0
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         if counter < k:
        #             counter += 1
        #             indexes.add(i)
        #         else:
        #             if start in indexes:
        #                 indexes.remove(start)
        #                 indexes.add(i)
        #             else:
        #                 count -= 1
        #             start += 1
        #     else:
        #         count += 1
        #     maxcount = max(maxcount , count)
        # return maxcount

        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len
