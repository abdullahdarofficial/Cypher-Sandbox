class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def recurrence(i, j):
            if (i,j) in memo:
                return memo[(i,j)]

            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return recurrence(i + 1, j + 1)
            else:
                return 1 + min(
                    recurrence(i + 1, j),
                    recurrence(i, j + 1),
                    recurrence(i + 1, j + 1)
                )
            return memo[(i,j)]
        return recurrence(0,0)