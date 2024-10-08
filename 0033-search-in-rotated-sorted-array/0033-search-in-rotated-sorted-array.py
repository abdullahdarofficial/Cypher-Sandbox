class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binarySearch(left, right):
            if left <= right:

                mid = (left + right) //2

                if nums[mid] == target:
                    return mid

                if nums[mid] >= nums[left]: #left half is sorted
                    if nums[left] <= target < nums[mid]: #goto left half 
                        return binarySearch(left, mid - 1)
                    else:
                        return binarySearch(mid + 1, right)
                else:
                    if nums[right] >= target > nums[mid]:
                        return binarySearch(mid + 1, right)
                    else:
                        return binarySearch(left, mid - 1)
                    
            else:
                return -1

        return binarySearch(0, len(nums) - 1)