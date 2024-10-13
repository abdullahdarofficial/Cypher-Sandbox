class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Check if the mid element is greater than the next element
            if nums[mid] > nums[mid + 1]:
                # If it is, a peak must be on the left side (including mid)
                right = mid
            else:
                # If not, the peak must be on the right side
                left = mid + 1
        
        # When left == right, we've found a peak
        return left