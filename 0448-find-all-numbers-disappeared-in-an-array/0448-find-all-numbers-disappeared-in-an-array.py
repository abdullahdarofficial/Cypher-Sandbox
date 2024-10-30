class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        lis = []
        i = 1
        last = 0
        for num in nums:
            if last and last == num:
                continue
            if i != num:
                lis.append(i)
            last = num
            i += 1 
        while last < len(nums):
            last += 1
            lis.append(last)
        return lis