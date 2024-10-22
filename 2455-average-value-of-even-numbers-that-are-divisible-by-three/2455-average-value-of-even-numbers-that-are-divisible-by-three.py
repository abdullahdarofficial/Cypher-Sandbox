class Solution:
    def averageValue(self, nums: List[int]) -> int:

        count = 0
        currsum = 0

        for num in nums:
            if num % 3 == 0 and num > 3 and num % 2 == 0:
                currsum += num
                count += 1
                print(currsum, count)

        return currsum//count if count else 0

        