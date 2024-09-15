# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
       
#         first = 0
#         temp = 2
#         for i in range(len(nums)):
#             if first != i:
#                 if i - first != 1:
#                     if nums[first] != nums[i]:
#                         if i - first != 2:
#                             k = 2
#                             for j in range(i, len(nums)):
#                                 nums[first + k] = nums[j]
#                                 k += 1
#                             first += 2
#                             i = first
#                         else:
#                             first = i
#                     else:
#                         if first != 0:
#                             temp = first + 1
#                         else:
#                             temp = first + 2
#                 else:
#                     if nums[first] != nums[i]:
#                        first += i
#         print(temp, first)
#         if temp > first:
#             return temp
#         return first + 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        insert_pos = 2  # Start at the third position
        for i in range(2, len(nums)):
            if nums[i] != nums[insert_pos - 2]:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        return insert_pos
