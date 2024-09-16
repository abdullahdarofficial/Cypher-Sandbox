class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        i = 0
        j = 0
        current = nums[0]
        count = len(nums) + 1
        while i <= j and i < len(nums):
            if current >= target:
                if (j - i + 1) < count:
                    count = j - i + 1
                if i != j:
                    current -= nums[i]
                    i += 1

                else:
                    current -= nums[i]
                    i += 1
                    j += 1
                    if j < len(nums):
                        current += nums[j]
                    else:
                        if target > current:
                            break

            else:
                j += 1
                if j < len(nums):
                    current += nums[j]
                else:
                    if target > current:
                        break

        if count > len(nums):
            return 0
        else:
            return count


