class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        

        if not nums or len(nums) < k:
            return None
        
        start = 0
        end = k
        max_sum = 0
        for i in range(k):
            max_sum += nums[i]
        print(max_sum)
        curr_sum = max_sum
        for i in range(end, len(nums)):
            curr_sum = curr_sum - nums[start] + nums[i]
            start += 1
            max_sum = max(max_sum, curr_sum)
            print(max_sum)

        return max_sum / k