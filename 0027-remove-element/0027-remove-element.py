class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0  # Pointer to track position for non-val elements
        for j in range(len(nums)):  # Iterate over the array
            if nums[j] != val:
                # Place the non-val element at the i-th index and increment i
                nums[i] = nums[j]
                i += 1
        return i
