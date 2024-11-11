class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        def binarySearch(arr, num):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right)//2
               
                if arr[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        dp = []

        for num in nums:
            pos = binarySearch(dp, num)
            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num
        return len(dp)

    