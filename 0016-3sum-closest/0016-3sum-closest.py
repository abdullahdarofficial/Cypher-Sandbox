class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        bestSoFar = float('inf')

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                currsum = nums[i] + nums[j] + nums[k]
                
                if abs(currsum - target) < abs(bestSoFar - target):
                    bestSoFar = currsum

                if currsum < target:
                    j += 1
                elif currsum > target:
                    k -= 1
                else:
                    return currsum  # If currsum is exactly the target

        return bestSoFar
