class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        left = 0
        true = k
        maxsize = 0
        for right in range(left, len(answerKey)):
            if answerKey[right] == 'F':
                if true:
                    true -= 1
                else:
                    while answerKey[left] != 'F':
                        left += 1
                    left += 1
            maxsize = max(maxsize, right - left + 1)
        left = 0
        false = k
        for right in range(left, len(answerKey)):
            if answerKey[right] == 'T':
                if false:
                    false -= 1
                else:
                    while answerKey[left] != 'T':
                        left += 1
                    left += 1
            maxsize = max(maxsize, right - left + 1)
        return maxsize


