class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        
     
        num_to_index = {}  # Dictionary to store number and its index
        for i, num in enumerate(nums):
            complement = target - num  # The number needed to reach the target
            if complement in num_to_index:  # Check if complement is in dictionary
                return [
                    num_to_index[complement],
                    i,
                ]  # Return indices of complement and current num
            num_to_index[num] = i  # Store the index of the current number
