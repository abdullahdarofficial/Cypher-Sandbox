class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        counts = Counter(s)
        print(counts)
        result = 0
        maxsum = 0
        oddcount = 0
        for char, val in counts.items():
            if val % 2 != 0:
                oddcount += 1
            result += val
        return result - oddcount + 1 if oddcount > 1 else result