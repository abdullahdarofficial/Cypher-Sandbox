class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ones, twos = 0, 0
        for num in nums:
            twos |= ones & num # those bits that appeared once and again come in num add them also in twos
            ones ^= num # any bits that appears odd num times will be in ones
            threes = ones & twos # all bits appeared in twos and ones means that are 3 time appeared
            ones &= ~threes # keep only those bits that are not in three but in ones
            twos &= ~threes # keep only those bits that are not in three but in twos
        return ones
