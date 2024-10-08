class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # map = {}
        # size = len(nums)

        # for num in nums:
        #     count = 1
        #     currnum = num
        #     while currnum - 1 in map:
        #         currnum -= 1
        #         count += 1
        #     currnum = num
        #     while currnum + 1 in map:
        #         currnum += 1
        #         count += 1

        #     map[num] = count
        
        # return map[max(map, key = map.get)]

        # if not nums:
        #     return 0

        # map = set()
        # size = len(nums)
        # maxcount = 0
        # for num in nums:
        #     count = 1
        #     currnum = num
        #     while currnum - 1 in map:
        #         currnum -= 1
        #         count += 1
        #     currnum = num
        #     while currnum + 1 in map:
        #         currnum += 1
        #         count += 1
        #     if maxcount < count:
        #         maxcount = count
        
        # return maxcount

        if not nums:
            return 0

        num_set = set(nums)
        max_count = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_count = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_count += 1
                
                max_count = max(max_count, curr_count)


        return max_count