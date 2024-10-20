class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        # Initialize dp_even and dp_odd based on the first element
        if nums[0] % 2 == 0:
            dp_even = nums[0]
            dp_odd = float('-inf')  # Cannot start with an odd number
        else:
            dp_odd = nums[0]
            dp_even = float('-inf')  # Cannot start with an even number

        # Traverse the array
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                # nums[i] is even: update dp_even
                dp_even = max(dp_even + nums[i], dp_odd + nums[i] - x)
            else:
                # nums[i] is odd: update dp_odd
                dp_odd = max(dp_odd + nums[i], dp_even + nums[i] - x)

        # Return the maximum score from both dp_odd and dp_even
        return max(dp_even, dp_odd)
