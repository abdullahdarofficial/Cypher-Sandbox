class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        num = 0
        for x in nums:
            num = num ^ x
        
        return num
