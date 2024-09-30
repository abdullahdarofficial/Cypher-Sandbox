class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        if not s or len(s) < k:
            return 0
        
        start = 0
        vowels = "aeiou"
        maxcount = 0
        for i in range(k):
            if s[i] in vowels:
                maxcount += 1
        currcount = maxcount
        for i in range(k, len(s)):
            print(maxcount, currcount, start, i)
            if s[start] in vowels:
                currcount -= 1
            if s[i] in vowels:
                currcount += 1
            start += 1
            maxcount = max(maxcount, currcount)
        return maxcount                


        
