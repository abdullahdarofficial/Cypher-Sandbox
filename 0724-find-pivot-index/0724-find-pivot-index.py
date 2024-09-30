class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # if not nums or len(nums) == 1:
        #     return -1

        # left = 0
        # right = len(nums) - 1
        # sumleft = nums[left]
        # sumright = nums[right]
        # print(sumleft, sumright)

        # while left < right:
        #     if abs(sumleft) > abs(sumright):
        #         right -= 1
        #         sumright += nums[right]
        #     else:
        #         left += 1
        #         sumleft += nums[left]
        #     print(sumleft, sumright)

        # if sumleft == sumright:
        #     if left == right:
        #         return left
        #     else:
        #         return -1
        # return -1

        totalSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum = totalSum - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]

        return -1

        

        