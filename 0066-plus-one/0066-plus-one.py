class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) -1 
        num = 1
        while i >= 0:
            curr = digits[i] + num
            if curr < 10:
                digits[i] = curr
                return digits
            else:
                digits[i] = curr % 10
                num = curr // 10
            i-=1

        digits.append(0)
        for i in range(len(digits) - 1):
            digits[i + 1] = digits[i]
        digits[0] = num
        return digits