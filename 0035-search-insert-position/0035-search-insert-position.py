# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
        
#         def binarySearch(left, right):

#             if left < right:
#                 mid = (left + right) // 2

#                 if nums[mid] == target:
#                     return mid

#                 elif nums[mid] > target:
#                     return binarySearch(left, mid - 1)
#                 else:
#                     return binarySearch(mid + 1, right)
#             # elif left == right:
#             else:
#                 if nums[left] >= target:
#                     return left
#                 return left + 1
#             # else:
#             #     return 0 
            
#         return binarySearch(0, len(nums) - 1)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binarySearch(left, right):

            if left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid

                elif nums[mid] > target:
                    return binarySearch(left, mid - 1)
                else:
                    return binarySearch(mid + 1, right)
            else:
                return left 
            # else:
            #     return 0 
            
        return binarySearch(0, len(nums) - 1)
